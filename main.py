from flask import Flask, flash, request, redirect, url_for, render_template
from ocr import *
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet
import os

UPLOAD_FOLDER = '/documents/github/rec-iept/static/uploadfolder'
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("receipt.html")

photos = UploadSet('photos', IMAGES)
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Photo saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('upload.html', user_image = request.form['photo'])

@app.route('/photo/<id>')
def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)


if __name__ == "__main__":
    app.run(debug=True)