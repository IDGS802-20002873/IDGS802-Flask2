from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField
from wtforms.fields import EmailField, PasswordField
from wtforms import validators

def mi_validacion(form, field):
    if len(field.data)==0:
        raise validators.ValidationError['El campo no tiene datos']

class UserForm(Form):
    
    matricula = StringField('Matricula',[
        validators.DataRequired(message= 'La matricula es requerida')])
    nombre = StringField('Nombre',[
        validators.DataRequired(message= 'El nombre es requerido'),
        validators.length(min=15, message='Ingresa un valor maximo')])
    apaterno = StringField('Apaterno',[mi_validacion])
    amaterno = StringField('Amaterno',[
        validators.DataRequired(message= 'El apellido Materno es requerida')])
    email = EmailField('Correo',[
        validators.DataRequired(message= 'El correo es requerido')])
    

class LoginForm(Form):
    username = StringField('Usuario',[validators.DataRequired(message= 'El usuario es requerida')])
    password = PasswordField('Contraseña',[validators.DataRequired(message= 'El campo es requerido'),validators.length(min=15, message='Ingresa un valor maximo')])