from app.application import ApplicationForm, Application

from flask import Blueprint, render_template, redirect, url_for, flash

# Create a blueprint for the application
applybp = Blueprint("applybp", __name__)


@applybp.route('/apply', methods=["GET", "POST"])
def apply_now():
    form = ApplicationForm()
    if form.validate_on_submit():
        # TODO: Save the form to db
        flash('Your application has been submitted successfully.')
        return redirect(url_for('index'))
    # Default invalid provider ID (will get caught in form validation)
    provider = -1
    if 'provider' in request.args:
        provider = int(request.args['provider'])
    return render_template('apply.html', form=form, provider=provider, title="Apply Now")
