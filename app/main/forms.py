from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import Required
# from wtforms import ValidationError


class UploadForm(Form):
    file = FileField("Upload And Dockerize")
    upload = SubmitField("Upload")


class GithubForm(Form):
    github_auth = SubmitField("Authenticate with Github")
    github_client_id = StringField('Github Client ID', validators=[Required()])
    github_client_secret = StringField('Github Client Secret', validators=[Required()])
