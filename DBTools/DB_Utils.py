import mysql.connector

# a function to create connection to database and return connection object
def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin-pass",
        database="CareerConnect"
    )
    return mydb

# a function to close connection to database
def close_connection(mydb):
    mydb.close()


# a function to execute query and return result
def execute_query(mydb, query):
    cursor = mydb.cursor()
    cursor.execute(query)
    return cursor

# a function to commit changes to database
def commit_changes(mydb):
    mydb.commit()
    