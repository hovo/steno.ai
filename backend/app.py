from flask import Flask, jsonify, request
from google.cloud import storage

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    f = request.files['file']
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("steno")
    blob = bucket.blob(f.filename)
    blob.upload_from_file(f)

    return jsonify()
    
if __name__ == "__main__":
    app.run(port=8000)