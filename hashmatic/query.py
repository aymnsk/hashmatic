import sqlite3


def retrieve_from_database():
    conn = sqlite3.connect('captions.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Captions')
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"ID: {row[0]}, Image Path: {row[1]}, Caption: {row[2]}, Hashtags: {row[3]}, User ID: {row[4]}, Username: {row[5]}, Platform: {row[6]}")
    
    conn.close()
