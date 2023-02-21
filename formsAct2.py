from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField
from wtforms.fields import EmailField, PasswordField
from wtforms import validators

class LenguajeForm(Form):
    
    spanish = StringField('Español',[
        validators.DataRequired(message= 'El valor es requerido')])
    english = StringField('Ingles',[
        validators.DataRequired(message= 'El valor es requerido'),
        validators.length(min=15, message='Ingresa un valor maximo')])
    search = StringField('Buscar',[
        validators.DataRequired(message= 'El valor es requerido'),
        validators.length(min=15, message='Ingresa un valor maximo')])
    