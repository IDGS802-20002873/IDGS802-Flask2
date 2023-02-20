from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField,EmailField
from wtforms.fields import EmailField,TextAreaField,PasswordField
from wtforms import validators

class UserForm(Form):
    numero = StringField('Numero',[validators.DataRequired(message='Numero requerido')])