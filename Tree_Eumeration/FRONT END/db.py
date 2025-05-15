import sqlite3

# Create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('users.db')  # Replace with your actual database file path if needed
    return conn

# Create the users table if it doesn't already exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, 
            email TEXT, 
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert a new user into the users table
def insert_user(username, email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, email, password))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        # Handle the case where the username already exists
        return False
    return True

# Validate user credentials during login
def validate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                   (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Create the table if it doesn't exist already (this ensures the table is created when the app starts)
create_table()
