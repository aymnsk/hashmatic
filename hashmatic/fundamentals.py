# write a program for A.I using python that  scans the given image or video and auto generates caption and hashtags in English 


import cv2
import numpy as np
import tensorflow as tf
from transformers import pipeline
from PIL import Image

# Load the image or video
def load_media(media_path):
    if media_path.endswith(('.jpg', '.png', '.jpeg')):
        return Image.open(media_path)
    elif media_path.endswith(('.mp4', '.avi')):
        cap = cv2.VideoCapture(media_path)
        ret, frame = cap.read()
        cap.release()
        if ret:
            return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    else:
        raise ValueError("Unsupported file format.")

# Initialize the image captioning model
caption_generator = pipeline("image-captioning")

# Generate caption
def generate_caption(image):
    caption = caption_generator(image, max_length=30)[0]['caption']
    return caption

# Generate hashtags from caption
def generate_hashtags(caption):
    words = caption.split()
    hashtags = [f'#{word.lower()}' for word in words if len(word) > 3]
    return hashtags

# Main function
def process_media(media_path):
    image = load_media(media_path)
    caption = generate_caption(image)
    hashtags = generate_hashtags(caption)
    return caption, hashtags

# Example usage
if __name__ == "__main__":
    media_path = 'path_to_your_image_or_video.jpg'  # Change to your file path
    caption, hashtags = process_media(media_path)
    print("Caption:", caption)
    print("Hashtags:", ' '.join(hashtags))



# Creating a program to generate captions and hashtags for images or videos involves several steps, including loading the image or video, processing it with a pre-trained model for image recognition, and generating captions and hashtags based on the identified objects or scenes. Here's a simplified version using Python, leveraging libraries like TensorFlow/Keras, OpenCV, and transformers for natural language processing.

# ### Requirements
# Before you start, make sure you have the following packages installed:

# ```bash
# pip install tensorflow opencv-python transformers Pillow
# ```

# ### Code Example

# Here’s a basic example that outlines how to implement this functionality:

# ```python
# import cv2
# import numpy as np
# import tensorflow as tf
# from transformers import pipeline
# from PIL import Image

# # Load the image or video
# def load_media(media_path):
#     if media_path.endswith(('.jpg', '.png', '.jpeg')):
#         return Image.open(media_path)
#     elif media_path.endswith(('.mp4', '.avi')):
#         cap = cv2.VideoCapture(media_path)
#         ret, frame = cap.read()
#         cap.release()
#         if ret:
#             return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     else:
#         raise ValueError("Unsupported file format.")

# # Initialize the image captioning model
# caption_generator = pipeline("image-captioning")

# # Generate caption
# def generate_caption(image):
#     caption = caption_generator(image, max_length=30)[0]['caption']
#     return caption

# # Generate hashtags from caption
# def generate_hashtags(caption):
#     words = caption.split()
#     hashtags = [f'#{word.lower()}' for word in words if len(word) > 3]
#     return hashtags

# # Main function
# def process_media(media_path):
#     image = load_media(media_path)
#     caption = generate_caption(image)
#     hashtags = generate_hashtags(caption)
#     return caption, hashtags

# # Example usage
# if __name__ == "__main__":
#     media_path = 'path_to_your_image_or_video.jpg'  # Change to your file path
#     caption, hashtags = process_media(media_path)
#     print("Caption:", caption)
#     print("Hashtags:", ' '.join(hashtags))
# ```

# ### Explanation
# 1. **Load Media**: The `load_media` function loads either an image or a video and extracts a single frame from the video.
# 2. **Caption Generation**: The `generate_caption` function uses the Hugging Face Transformers library to create a caption for the image.
# 3. **Hashtag Generation**: The `generate_hashtags` function creates hashtags from the caption by converting each word to lowercase and prepending a `#`.
# 4. **Main Function**: The `process_media` function combines all the steps and returns the generated caption and hashtags.

# ### Running the Code
# 1. Replace `path_to_your_image_or_video.jpg` with the path to your media file.
# 2. Run the script, and it will print the generated caption and hashtags.

# ### Notes
# - You may want to refine the hashtag generation logic based on your specific requirements.
# - The model used for captioning might require downloading the model weights upon first use.
# - Consider enhancing the error handling and input validation for production-level code.