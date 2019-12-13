from app.application import ApplicationForm, Application

from flask import Blueprint, render_template, redirect, url_for, flash, request

# Create a blueprint for the application
applybp = Blueprint("applybp", __name__)

from app import db


@applybp.route('/apply', methods=["GET", "POST"])
def apply_now():
    form = ApplicationForm()
    if form.validate_on_submit():
        # TODO: Save the form to db
        application = Application(
            provider=int(form.provider.data),
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            initial_purchase=form.initial_purchase_amt.data,
            address=form.address.data,
            housing_type=form.housing_type.data,
            phone=form.phone.data,
            phone_type=form.phone_type.data,
            email=form.email.data,
            ssn=form.ssn.data,
            dob=form.dob.data
        )
        db.session.add(application)
        db.session.commit()
        flash('Your application has been submitted successfully.')
        return redirect(url_for('index'))
    # Default invalid provider ID (will get caught in form validation)
    provider = -1
    if 'provider' in request.args:
        provider = int(request.args['provider'])
    return render_template('apply.html', form=form, provider=provider, title="Apply Now")
