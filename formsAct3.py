from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField
from wtforms.fields import EmailField, PasswordField
from wtforms import validators

class Resistencias(Form):
    b1=SelectField(u'Resistencia 1', [validators.DataRequired(message='La banda 1 es requerida')],
                  choices=[(0, 'Negro'), (1, 'Café'),
                           (2, 'Rojo'), (3, 'Naranja'),
                           (4, 'Amarillo'), (5, 'Verde'),
                           (6, 'Azul'), (7, 'Violeta'),
                           (8, 'Gris'), (9, 'Blanco')])
    b2=SelectField(u'Resistencia 2', [validators.DataRequired(message='La banda 2 es requerida')],
                  choices=[(0, 'Negro'), (1, 'Café'),
                           (2, 'Rojo'), (3, 'Naranja'),
                           (4, 'Amarillo'), (5, 'Verde'),
                           (6, 'Azul'), (7, 'Violeta'),
                           (8, 'Gris'), (9, 'Blanco')])
    b3=SelectField(u'Multiplicador', [validators.DataRequired(message='El multiplicador es requerido')],
                  choices=[(1, 'Negro'), (10, 'Café'),
                           (100, 'Rojo'), (1000, 'Naranja'),
                           (10000, 'Amarillo'), (100000, 'Verde'),
                           (1000000, 'Azul'), (10000000, 'Violeta'),
                           (100000000, 'Gris'), (1000000000, 'Blanco')])
    tolerancia =  RadioField('Tolerancia:', [validators.DataRequired(message='La tolerancia es requerida')],
                         choices=[(1,'Dorado'),(0,'Plata')])