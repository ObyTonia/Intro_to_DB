import mysql.connector

def create_database(host, user, password, database_name):
    """
    Attempts to create a database with the given name on the MySQL server.

    Args:
        host (str): The hostname or IP address of the MySQL server.
        user (str): The username for connecting to the MySQL server.
        password (str): The password for the specified user.
        database_name (str): The name of the database to be created.

    Returns:
        None

    Prints:
        - Success message if the database is created successfully.
        - Error message if there's an issue connecting or creating the database.
    """

    try:
        # Establish connection to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # Create database using CREATE DATABASE IF NOT EXISTS syntax
        create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
        cursor.execute(create_database_query)

        connection.commit()  # Commit the database creation

        print(f"Database '{database_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    finally:
        if connection:
            connection.close()  # Close the connection regardless of success or failure

# Replace with your actual MySQL server credentials
host = "localhost"
user = "your_username"
password = "your_password"
database_name = "alx_book_store"

create_database(host, user, password, database_name)