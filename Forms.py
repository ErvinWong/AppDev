from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField

class CreateUserForm(Form):
    first_name = StringField('Product ID', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Quantity', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Type', [validators.DataRequired()], choices=[('', 'Select'), ('R', 'Racket'), ('S', 'Shoes'), ('C','Clothing')], default='')
    membership = RadioField('Availability', choices=[('Y', 'Yes'), ('N', 'No')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()], default='')

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Free'), ('P', 'Premium')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
