from flask.ext.wtf import Form
from wtforms import FileField, SubmitField
# from wtforms.validators import Required
# from wtforms import ValidationError


class UploadForm(Form):
    file = FileField("Upload And Dockerize")
    upload = SubmitField("Upload")
