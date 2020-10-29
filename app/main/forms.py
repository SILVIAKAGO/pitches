from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    ''' Create a wtf form for creating pitches '''

    content = TextAreaField('Your Pitch')
    submit = SubmitField('Submit')

class CommentForm (FlaskForm):
    ''' Create a wtf form for creating a pitch '''
    opinion = TextAreaField('write comment')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    ''' create a wtf form for creating a pitch '''
    name = StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')


