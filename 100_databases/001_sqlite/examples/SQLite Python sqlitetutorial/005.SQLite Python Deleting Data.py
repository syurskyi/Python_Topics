# Summary: this tutorial shows you how to delete data in the SQLite database
# from a Python program using the sqlite3 module.
#
# In order to delete data in the SQLite database from a Python program, you use the following steps:
#
#     First, establish a connection the SQLite database by creating a Connection object using the connect() function.
#     Second, to execute a DELETE statement, you need to create a Cursor object using the cursor()
#     method of the Connection object.
#     Third, execute the  DELETE statement using the execute() method of the Cursor object.
#     In case you want to pass the arguments to the statement, you use a question mark ( ?) for each argument.
#
# The following  create_connection() function establishes a database connection to an SQLite database
# specified by a database file name:

import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# The following delete_task() function deletes a task in the tasks table by id.

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# The following delete_all_tasks() function deletes all rows in the tasks table.


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()