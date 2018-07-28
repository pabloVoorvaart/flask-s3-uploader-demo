from flask import Flask, flash, render_template, request
from flask_cdn import CDN
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object('config')
cdn = CDN(app)

class UploadForm(FlaskForm):
    image = FileField('image')
    submit = SubmitField('Create')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def file_upload():
    form = UploadForm()
    if form.validate_on_submit():
        file_upload = form.image.data
        file_name = secure_filename(file_upload.filename)
        if allowed_file(file_name):
            s3 = app.config['S3']
            file_upload.save(os.path.join('/tmp', file_name))
            s3.Object(app.config['BUCKET_NAME'], file_name).put(Body=open('/tmp/' + file_name, 'rb'))
            os.remove(os.path.join('/tmp', file_name))
            flash('file uploaded')
    return render_template('example.html', form=form)
