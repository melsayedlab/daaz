from flask import render_template, flash
from flask.ext.login import login_required
from .forms import UploadForm, GithubForm
from . import main
from .. import github
from dockerize import dockerize
from werkzeug import secure_filename


ALLOWED_EXTENSIONS = set(['zip'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    uploadform = UploadForm()
    githubform = GithubForm()
    if uploadform.validate_on_submit():
        if uploadform.file and allowed_file(uploadform.file.data.filename):
            filename = secure_filename(uploadform.file.data.filename)
            uploadform.file.data.save('/tmp/' + filename)
            cntnr_id = dockerize('/tmp/' + filename)
            flash("The app has been Dockerized..")
        if githubform.validate_on_submit():
            return github.authorize()
        else:
            flash("Error! You are trying to upload wrong extension")
    return render_template('index.html', uploadform=uploadform, githubform=githubform)
