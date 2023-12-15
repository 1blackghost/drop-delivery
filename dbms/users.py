import sqlite3
import json
import random

DATABASE_NAME = 'users.db'

def connect_to_database():
    return sqlite3.connect(DATABASE_NAME, check_same_thread=False)

def reset_back_to_start():
    with connect_to_database() as conn:
        c = conn.cursor()
        print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
        a = input()
        c.execute("DROP TABLE IF EXISTS user")
        if a in ("y", "yes"):
            c.execute('''CREATE TABLE IF NOT EXISTS user
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        number INTEGER UNIQUE,
                        preferences TEXT CHECK(preferences IN ('Malayalam', 'English')),
                        additional_data TEXT DEFAULT NULL
                        )''')

def insert_user(number, preferences, additional_data=None):
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO user (number, preferences, additional_data) VALUES (?, ?, ?)",
                  (number, preferences, json.dumps(additional_data) if additional_data else None))

def read_users():
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM user")
        result = c.fetchall()
    return result

def read_user_by_id(user_id):
    with connect_to_database() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE id=?", (user_id,))
        result = c.fetchone()
    return result

def update_user(user_id, preferences=None, additional_data=None):
    with connect_to_database() as conn:
        c = conn.cursor()

        update_query = "UPDATE user SET "
        update_values = []

        if preferences is not None:
            update_query += "preferences=?, "
            update_values.append(preferences)

        if additional_data is not None:
            update_query += "additional_data=?, "
            update_values.append(json.dumps(additional_data))

        # Remove the trailing comma and space
        update_query = update_query.rstrip(", ")

        # Add the WHERE clause to update based on the user ID
        update_query += " WHERE id=?"

        # Add the user ID value to the update_values list
        update_values.append(user_id)

        # Execute the update query
        c.execute(update_query, tuple(update_values))

# Example usage:
# reset_back_to_start()
# insert_user(123, 'Malayalam', {'key': 'value'})
# insert_user(456, 'English', {'key': 'another_value'})
# update_user(1, preferences='English', additional_data={'new_key': 'new_value'})
# users = read_users()
# specific_user = read_user_by_id(1)
