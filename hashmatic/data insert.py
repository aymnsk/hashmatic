import sqlite3


def save_to_database(image_path, video_path, caption, hashtags, user_id=None, username=None, platform=None):
    conn = sqlite3.connect('captions.db')
    cursor = conn.cursor()
    
    # Convert hashtags list to a comma-separated string
    hashtags_str = ', '.join(hashtags)

    # Insert the data into the table
    cursor.execute('''
        INSERT INTO Captions (image_path, caption, hashtags, user_id, username, platform)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (image_path, video_path, caption, hashtags_str, user_id, username, platform))
    
    conn.commit()
    conn.close()

