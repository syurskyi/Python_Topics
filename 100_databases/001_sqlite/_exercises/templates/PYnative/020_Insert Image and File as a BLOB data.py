_____ ?

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') __ file:
        blobData _ file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ sqliteConnection.c..
        print("Connected to SQLite")
        sqlite_insert_blob_query _ """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto _ convertToBinaryData(photo)
        resume _ convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple _ (empId, name, empPhoto, resume)
        cursor.e..(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.c..

    _____ ?.E.. __ error:
        print("Failed to insert blob data into sqlite table", error)
    f..
        __ (sqliteConnection):
            sqliteConnection.c..
            print("the sqlite connection is closed")

insertBLOB(1, "Smith", "E:\pynative\Python\photos\smith.jpg", "E:\pynative\Python\photos\smith_resume.txt")
insertBLOB(2, "David", "E:\pynative\Python\photos\david.jpg", "E:\pynative\Python\photos\david_resume.txt")


# Output:
#
# Connected to SQLite
# Image and file inserted successfully as a BLOB into a table
# the sqlite connection is closed
# Connected to SQLite
# Image and file inserted successfully as a BLOB into a table
# the sqlite connection is closed