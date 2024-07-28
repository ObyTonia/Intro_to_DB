import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change this if your MySQL server is on a different host
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # SQL query to create a database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()