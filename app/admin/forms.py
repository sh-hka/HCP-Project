from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField, FileRequired
from wtforms import ValidationError
from app.provider.models import Provider

CSV_SCHEMA = None
DB_SCHEMA = [item for item in dir(Provider) if '__' not in item]  # Remove builtin functions from the list


class FileSizeValidator(object):
    def __init__(self, message=None, max_size=5*1024*1024):  # 5MB
        self.max_size = max_size
        if message is None:
            message = u'The file size exceeded max_size({})'.format(self.max_size)
        self.message = message

    def __call__(self, form, field):
        if field.data:
            file_size = len(field.data.stream.read())
            field.data.stream.seek(0)  # Cleanup for the user
            if file_size > self.max_size:
                raise ValidationError(self.message)


class CSVFileValidator(object):
    def __init__(self, mime_message=None, header_message=None):
        if mime_message is None:
            mime_message = u'The provided file is not a CSV file.'
        self.mime_message = mime_message
        if header_message is None:
            header_message = u'The provided CSV file does not conform to the database schema.' \
                            + u' Illegal column in CSV: {}'
        self.header_message = header_message

    def __call__(self, form, field):
        global CSV_SCHEMA
        if field.data:
            if field.data.mimetype != 'text/csv':
                raise ValidationError(self.mime_message)

            # Check that the uploaded CSV matches our schema
            CSV_SCHEMA = field.data.stream.readline().decode('utf-8').strip().split(',')  # yikes. This creates a list
                                                                                          # of the schema.
            field.data.stream.seek(0)  # Cleanup for the user
            for item in CSV_SCHEMA:
                if item not in DB_SCHEMA:
                    raise ValidationError(self.header_message.format(item))


class ProviderImportForm(Form):
    file = FileField(validators=[FileRequired(), FileSizeValidator(), CSVFileValidator()],
                     description="Import Provider data from CSV file.")
