from flask_wtf import Form
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired, Length

def phone_check(form, field):
    phone = field.data
    if len(phone) != 10:
        raise ValidationError('Phone field must be 10 digits long.')
     
    if not phone.isnumeric():
        raise ValidationError('Phone field must only contains digits.')
     
    if not(phone.startswith("0")):
        raise ValidationError('Phone field must be a valid french number (starting with 0)')


class ContactForm(Form):
    """
    A helper to validate form

    The contact form contains 4 fields.
    Three of whicn are mandatory.
    """
    name = StringField("name", [DataRequired(message="Hey buddy! What's your name ?")])
    fname = StringField("fname", [DataRequired(message="We need your first name, don't be shy.")])
    phone = StringField("phone", [DataRequired(), phone_check])
    speech = StringField("speech")
