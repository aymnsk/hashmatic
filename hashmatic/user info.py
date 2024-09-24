import sqlite3


def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('captions.db')
    cursor = conn.cursor()
    
    # Create a table to store captions and hashtags
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Captions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT NOT NULL,
            video_path TEXT,      
            caption TEXT NOT NULL,
            hashtags TEXT NOT NULL,
            user_id TEXT,
            username TEXT,
            platform TEXT
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

create_database()
