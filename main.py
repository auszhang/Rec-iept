from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import ocr, json

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)


# UPLOAD_FOLDER = 'uploadfolder'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)


filename = ""
item_price = {}

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
    	filename = photos.save(request.files['photo'])
    	pather = 'static/img/' + str(filename)
    	item_price = ocr.mainer(pather)
    	json.dumps(item_price)
    	return render_template('breakdown.html', dict1 = {"name":1,"assd":2})
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)