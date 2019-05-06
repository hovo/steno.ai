from flask import Flask, jsonify, request
import file_service as fs

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    f = request.files['file']
    fs.upload_to_gcs(f)

    return jsonify()

if __name__ == "__main__":
    app.run(port=8000)