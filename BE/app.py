from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Define the route to check copyright
@app.route('/api/check-copyright', methods=['POST'])
def check_copyright():
    # Get the file from the request
    image = request.files.get('image')
    
    # If no image is provided, return an error message
    if not image:
        return jsonify({'result': 'No image provided'}), 400

    # Dummy logic to check if the filename contains 'copyright'
    if 'copyright' in image.filename.lower():
        return jsonify({'result': 'Copyright Infringed'})
    
    # If there's no issue, return 'No Issue'
    return jsonify({'result': 'No Issue'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)