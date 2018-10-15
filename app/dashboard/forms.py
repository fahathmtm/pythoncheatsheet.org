from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.validators import Length
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    administrator = BooleanField('Administrator')

    def validate_username(self, username):
        """
        Check if a user exists or not. If Exists, Raise ValidationError.
        """

        user = User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """
        Check if an Email exists or not. If Exists, Raise ValidationError.
        """

        user = User.query.filter_by(email=email.data).first()

        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2)])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=500)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    screen_name = StringField('Screen Name', validators=[DataRequired()])
    website = StringField('Website')
    github = StringField('GitHub')
    twitter = StringField('Twitter')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        """
        Check if a user exists or not. If Exists, Raise ValidationError.
        """

        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()

            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=2, max=280)])
    url = StringField('Title', validators=[
                      DataRequired(), Length(min=5, max=280)])
    markdown_url = StringField('Markdown URL', validators=[
                               DataRequired(), Length(min=10)])
    tags = StringField('Tags', validators=[DataRequired(), Length(min=2)])
    img_url = StringField('Image URL')
    summary = TextAreaField('Summary', validators=[
        DataRequired(), Length(min=50)])


class PinMsgForm(FlaskForm):
    home_msg = TextAreaField('Home Message', validators=[
        DataRequired(), Length(min=1, max=4000)])
    home_enable = BooleanField('Enable')
