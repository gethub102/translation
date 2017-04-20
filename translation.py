import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    sentence = request.get_data()
    # Call your function here to translate the sentence(string), and return the result in string
    result = 'Translated!'
    return result


@app.route('/evaluate', methods=['GET', 'POST'])
def elaluate():
    if request.method == 'POST':
        source = request.files['source']
        reference = request.files['reference']
        if source and reference and \
                allowed_file(source.filename) and allowed_file(reference.filename):
            source_name = secure_filename(source.filename)
            source_file_path = os.path.join(app.config['UPLOAD_FOLDER'], source_name)
            source.save(source_file_path)

            reference_name = secure_filename(reference.filename)
            reference_file_path = os.path.join(app.config['UPLOAD_FOLDER'], reference_name)
            reference.save(reference_file_path)

            # Call your function to evaluate the two files located at 'source_file_path' and 'reference_file_path',
            # and return a string.
            result = 'Evaluated!'
            return result

    return 'Error occurred!'


if __name__ == '__main__':
    app.run()
