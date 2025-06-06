from flask import Flask, render_template, request, jsonify
import os
from model.inference import run_inference

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        result = run_inference(filepath)
        return jsonify(result)

    return jsonify({'error': 'File upload failed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
