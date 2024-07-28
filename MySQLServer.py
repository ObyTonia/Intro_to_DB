import mysql.connector

def create_database(host, user, password, database_name):
    """
    Attempts to create a database with the given name on the MySQL server.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username for connecting to the MySQL server.
        password (str): The password for the user.
        database_name (str): The name of the database to create.

    Returns:
        None
    """

    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        cursor = connection.cursor()

        # Create database with IF NOT EXISTS to handle existing databases
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        cursor.execute(create_db_query)

        connection.commit()  # Commit changes to ensure database creation

        print(f"Database '{database_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    finally:
        if connection:
            connection.close()  # Always close the connection

# Replace with your actual MySQL server details
host = "localhost"
user = "your_username"
password = "your_password"
database_name = "alx_book_store"

create_database(host, user, password, database_name)