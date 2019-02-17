from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import ocr

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)


# UPLOAD_FOLDER = 'uploadfolder'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
    	filename = photos.save(request.files['photo'])
    	pather = 'static/img/' + str(filename)
    	return str(ocr.mainer(pather))
    return render_template('upload.html')
    #     file = request.files['image']
    #     f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        
    #     # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    #     file.save(f)

    # return render_template('end.html')

if __name__ == "__main__":
    app.run(debug=True)