from flask import Flask, request, jsonify

from fundamentals import process_media

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file temporarily
    file_path = f'temp/{file.filename}'
    file.save(file_path)

    # Process the media
    caption, hashtags = process_media(file_path)

    return jsonify({
        'caption': caption,
        'hashtags': hashtags
    })

if __name__ == '__main__':
    app.run(debug=True)






# Yes, the code provided is primarily a backend implementation. It processes images or videos to generate captions and hashtags using Python. Here are some key points regarding its role as backend code:

# 1. **Image/Video Processing**: The script handles media input and applies AI models to generate captions and hashtags, which is typical of backend processing.

# 2. **No User Interface**: It doesn't include a user interface (UI); instead, it takes a file path as input and prints the results to the console.

# 3. **AI Model Integration**: It utilizes pre-trained models for image captioning, which is often done on the server-side in backend applications.

# ### Possible Extensions
# To create a complete backend service, you might want to consider the following:

# - **API Development**: You can use a web framework like Flask or FastAPI to expose this functionality via an HTTP API.
  
# - **Deployment**: Consider deploying the application on a cloud service or server, where users can upload images or videos, and the backend processes them and returns the results.

# - **Error Handling**: Enhance error handling and validation for better user experience.

# ### Example: Basic Flask API
# Here’s a brief example of how you could wrap the existing functionality in a Flask API:

# ```python
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/generate', methods=['POST'])
# def generate():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     # Save the file temporarily
#     file_path = f'temp/{file.filename}'
#     file.save(file_path)

#     # Process the media
#     caption, hashtags = process_media(file_path)

#     return jsonify({
#         'caption': caption,
#         'hashtags': hashtags
#     })

# if __name__ == '__main__':
#     app.run(debug=True)
# ```

# ### Running the Flask API
# 1. Install Flask: `pip install Flask`.
# 2. Run the Flask app: `python your_flask_file.py`.
# 3. You can then send a POST request to `/generate` with an image or video file to get the caption and hashtags as a JSON response.