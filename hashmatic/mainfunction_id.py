def main(image_path, video_path=None, user_id=None, username=None, platform=None):
    caption, hashtags = generate_caption(image_path) # type: ignore
    
    print("Caption:", caption)
    print("Hashtags:", ['#' + label.replace(' ', '') for label in hashtags])

    # Save the generated caption and hashtags to the database
    save_to_database(image_path, video_path, caption, hashtags, user_id, username, platform) # type: ignore
    
if __name__ == "__main__":
    create_database()  # type: ignore # Ensure the database is created
    image_path = 'path/to/your/image.jpg'
    video_path = 'path/to/your/video.mp4'  # Optional
    # Example user info
    user_id = '12345'
    username = 'example_user'
    platform = 'Instagram'
    
    main(image_path, user_id, username, platform)
