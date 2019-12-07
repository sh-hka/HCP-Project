from app.views.application import ApplicationForm

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
    return render_template('apply.html', form=form, title="Apply Now")
