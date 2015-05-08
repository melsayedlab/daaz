from flask.ext.wtf import Form
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import Required
# from wtforms import ValidationError


class UploadForm(Form):
    file = FileField("Upload And Dockerize")
    upload = SubmitField("Upload")


class GithubForm(Form):
    github_repo_url = StringField('Github Repo URL', validators=[Required()])
    github_auth = SubmitField("Clone from Github")

