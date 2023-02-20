from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    required = StringField("(Required)")

    name = StringField("Name", validators=[InputRequired()])
    nameInput = StringField("Enter Your Full Name")

    email = StringField("Email", validators=[InputRequired(), Email()])
    emailInput = StringField("Enter Your E-Mail Address")

    subject = StringField("Subject", validators=[InputRequired()])
    subjectInput = StringField("Enter Subject")

    msg = TextAreaField('Message', validators=[InputRequired()])
    msgInput = StringField("Enter Your Message Here")

    submit = SubmitField("Send")