from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,PasswordField,BooleanField
from wtforms.validators import Required, Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    '''
    Registrationform that passes in the requires details for validatation
    '''
    email = StringField('Your email address', validators =[Required(), Email()])
    username = StringField('Your username', validators = [Required()])
    password = PasswordField('Password', validators= [Required(),EqualTo('password', message='passwords must match')])
    password_confirm = PasswordField('Confirm password', validators =[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
