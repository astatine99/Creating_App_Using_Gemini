from flask import Flask, request, render_template, redirect
import os

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/')
        
        file = request.files['file']
        if file.filename == '':
            return redirect('/')
        
        filename = file.filename
        filesize = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filetype = file.mimetype
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html', filename=filename, filesize=filesize, filetype=filetype, message='File uploaded successfully')
    

    
    else:
        return render_template('upload.html')
    
if __name__=='__main__':
    app.run(debug=True)

