from sqlalchemy.sql.elements import Null
from wtforms import Form
from wtforms import StringField, PasswordField,TextAreaField
from wtforms import validators
from wtforms.fields.simple import BooleanField, EmailField

from .models import User

def codi_validator(form,field):
    if field.data == 'codi' or  field.data=='CODI':
        raise validators.ValidationError('El username Codi no es permitido')


class LoginForm(Form):
    username = StringField('Username',[
        validators.length(min=5,max=15,message='El username no existe'),
        validators.DataRequired()
    ])
    password = PasswordField('Password',[
        validators.DataRequired(message='El password es requerido')
    ])

class RegisterForm(Form):

    username = StringField('Username',[
        validators.length(min=4,max=50),
        codi_validator
    
    ])
    email = EmailField('Email',[
        validators.length(min=5,max=100),
        validators.DataRequired(message='El email es requerido'),
        validators.Email(message='Ingrese un email valido')
    ])
    password = PasswordField('Password',[
        validators.DataRequired(message='El password es requerido')
    ])
    confirm_password = PasswordField('Confirm password',[
        validators.EqualTo('password',message='La contraseña no coincide')
    ])
    accept = BooleanField([
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El email ya se encuentra en uso')


    # def validate(self):
    #     if not Form.validate(self):
    #         return False

    #     if len(self.password.data)<3:
    #         self.password.errors.append('El password es demaciada corta')
    #         return False
    #     return 
        
class TaskForm(Form):
    title = StringField('Titulo',[
        validators.length(min=4,max=50,message='Titulo fuera de rango'),
        validators.DataRequired(message='El titulo esta vacio')
    ])
    description = TextAreaField('Descripcion',[
        validators.DataRequired('La descripcion es requerida')
    ],render_kw={'rows':5})

