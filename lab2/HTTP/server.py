from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found', 400
    file = request.files['file']

    return f'Succes'

if __name__ == '__main__':
    app.run()