import csv
from io import StringIO
import os.path as op

from flask import request, redirect, Response, flash, url_for
from werkzeug.exceptions import HTTPException
from flask_admin import Admin
from flask_admin.base import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from app import app, db
from app.provider import Provider
from app.application import Application
from app.admin import ProviderImportForm
from app.admin.forms import CSV_SCHEMA

admin = Admin(app, name="Admin", template_mode="bootstrap3")


class ModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization or request.environ.get(
            "REMOTE_USER")  # workaround for Apache
        if (not auth or
                (auth.username, auth.password) != app.config["ADMIN_CREDENTIALS"]):
            raise HTTPException(
                "",
                Response(
                    "You have to be an administrator.",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Login Required"'},
                ),
            )
        return True


class ApplicationView(ModelView):
    can_export = True


class ProviderView(ModelView):
    can_export = True
    list_template = 'admin/providers.html'  # Extending the list view to allow for CSV import

    @expose('/import', methods=['GET', 'POST'])
    def import_file(self):
        form = ProviderImportForm()
        if form.validate_on_submit():
            # form.file.data returns a Workzeug FileStorage object, .stream returns the tempfile w/CSV data in bytearray
            file_content = form.file.data.stream.read().decode('utf-8')
            with StringIO(file_content) as csv_file:
                csv_file_reader = csv.DictReader(csv_file, fieldnames=CSV_SCHEMA)
                for index, item in enumerate(csv_file_reader):
                    record = Provider(**{
                        'id': index,
                        'name': item['name'],
                        'speciality': item['speciality'],
                        'address': item['address'],
                        'city': item['city'],
                        'state': item['state'],
                        'zip': item['zip'],
                        'lat': float(item['lat']),
                        'lng': float(item['lng'])
                    })
                    # merge will update or insert if the entry does not exist
                    db.session.merge(record)
                db.session.commit()

            flash('Providers imported successfully.')
            return redirect(url_for('provider.index_view'))
        return self.render('admin/import.html', form=form)


# Applications
admin.add_view(ApplicationView(Application, db.session))

# Providers
admin.add_view(ProviderView(Provider, db.session))

# Static files
path = op.join(op.dirname(__file__), "../static")
admin.add_view(FileAdmin(path, "/static/", name="Static"))
