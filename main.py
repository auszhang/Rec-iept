from flask import Flask, render_template, request             
app = Flask(__name__)

UPLOAD_FOLDER = 'uploadfolder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("receipt.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        
        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)

    return render_template('end.html')



if __name__ == "__main__":
    app.run(debug=True)