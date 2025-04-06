from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/check-copyright', methods=['POST'])
def check_copyright():
    image = request.files.get('image')
    if not image:
        return jsonify({'error': 'No image provided'}), 400

    # Dummy logic to simulate detection
    file_id = str(uuid.uuid4())[:8]  # Short UUID
    if 'copyright' in image.filename.lower():
        verdict = 'Copyright Infringed'
        confidence = round(random.uniform(80.0, 99.9), 2)
    else:
        verdict = 'No Issue'
        confidence = round(random.uniform(90.0, 99.9), 2)

    return jsonify({
        'file_id': file_id,
        'verdict': verdict,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True)