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
namelist = []
item_name = {}

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
    	filename = photos.save(request.files['photo'])
    	pather = 'static/img/' + str(filename)
    	global item_price 
    	item_price = ocr.mainer(pather)
    	size = len(item_price)
    	return render_template('breakdown.html', dict1 = item_price)
    return render_template('upload.html')

@app.route('/breakdown', methods=['GET', 'POST'])
def breakdown():
	if request.method == 'POST':
		# print(str(item_price))
		i = 0
		for k,v in item_price.items():
			# print(request.form[])
			item_name[k] = request.form[k]
			# i += 1 
		return render_template('end.html', dict2 = item_name)
	return render_template('breakdown.html')

if __name__ == "__main__":
    app.run(debug=True)