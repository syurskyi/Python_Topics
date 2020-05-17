_____ ?  #Import the SQLite3 module
try:
    # Creates or opens a file called mydb with a SQLite3 DB
    db _ ?.c..('mydb.db')
    # Get a cursor object
    cursor _ db.c..
    # Check if table users does not exist and create it
    cursor.e..('''C.. T.. IF NOT EXISTS
                      users(id IN.. P.. K.., name T..., phone T..., email T... unique, password T...)''')
    # Commit the change
    db.c..
# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.c..

# We can use the Connection object as context manager to automatically commit or rollback transactions:

