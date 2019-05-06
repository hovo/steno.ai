from flask import Flask, jsonify, request
from file_service import get_metadata, upload_to_gcs, async_transcribe, poll_operation
from store import cache_metadata
import uuid
import json

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    gcs_uri = upload_to_gcs(file)

    # Generate an UUID for redis key
    id = str(uuid.uuid4())
    metadata = get_metadata(file)
    metadata['uri'] = gcs_uri
    val = json.dumps(metadata)

    # Cache file metadata on Redis
    cache_metadata(id, val)

    response = {"id": id}
    return jsonify(response)

@app.route('/api/transcribe/<id>', methods=['GET'])
def transcribe(id):
    operation = async_transcribe(id)
    return operation

@app.route('/api/operation/<name>', methods=['GET'])
def operation_status(name):
    response = poll_operation(name)
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=8000)