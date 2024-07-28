import mysql.connector

def create_database(db_name):
  """
  Creates the specified database in the MySQL server.

  Args:
      db_name (str): The name of the database to create.

  Prints success message or error message depending on the outcome.
  """
  try:
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )

    mycursor = mydb.cursor()

    # Create database
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    # Commit changes
    mydb.commit()

    print(f"Database '{db_name}' created successfully!")

  except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

  finally:
    # Close the connection
    if mydb:
      mydb.close()

if __name__ == "__main__":
  create_database("alx_book_store")