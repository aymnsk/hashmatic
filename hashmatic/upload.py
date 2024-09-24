import os
import tweepy
import requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Twitter authentication
def twitter_authenticate():
    auth = tweepy.OAuth1UserHandler(
        os.getenv('TWITTER_CONSUMER_KEY'), 
        os.getenv('TWITTER_CONSUMER_SECRET'), 
        os.getenv('TWITTER_ACCESS_TOKEN'), 
        os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    return tweepy.API(auth)

# Post to Twitter
def post_to_twitter(media_path, caption):
    api = twitter_authenticate()
    if media_path.endswith(('.mp4', '.mov')):
        api.update_status_with_media(status=caption, filename=media_path)
    else:
        api.update_status_with_media(status=caption, filename=media_path)

# Post to Facebook
def post_to_facebook(access_token, media_path, message):
    url = 'https://graph.facebook.com/v12.0/me/photos' if media_path.endswith(('.jpg', '.jpeg', '.png')) else 'https://graph.facebook.com/v12.0/me/videos'
    files = {'file': open(media_path, 'rb'), 'message': message}
    params = {'access_token': access_token}
    response = requests.post(url, files=files, params=params)
    return response.json()

# Post to Instagram
def upload_photo_to_instagram(media_path, caption):
    access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    user_id = os.getenv('INSTAGRAM_USER_ID')

    # Step 1: Upload the media
    url = f'https://graph.facebook.com/v12.0/{user_id}/media'
    with open(media_path, 'rb') as media_file:
        media_data = media_file.read()

    # Step 2: Create a media object
    response = requests.post(url, params={'access_token': access_token}, files={'file': media_data})
    media_id = response.json().get('id')

    # Step 3: Publish the media object
    publish_url = f'https://graph.facebook.com/v12.0/{user_id}/media_publish'
    publish_response = requests.post(publish_url, params={'access_token': access_token, 'creation_id': media_id})
    return publish_response.json()

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_to_all():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    caption = request.form.get('caption', '')
    platforms = request.form.getlist('platforms')

    # Save file temporarily
    media_path = f'temp_{file.filename}'
    file.save(media_path)

    # Upload to selected platforms
    responses = {}
    if 'twitter' in platforms:
        post_to_twitter(media_path, caption)
        responses['twitter'] = 'Posted to Twitter'
        
    if 'facebook' in platforms:
        post_to_facebook(os.getenv('FACEBOOK_ACCESS_TOKEN'), media_path, caption)
        responses['facebook'] = 'Posted to Facebook'

    if 'instagram' in platforms:
        upload_photo_to_instagram(media_path, caption)
        responses['instagram'] = 'Posted to Instagram'

    return jsonify({'message': 'Posted to selected platforms successfully!', 'responses': responses})

if __name__ == "__main__":
    app.run(debug=True)
