_____ ?

___ writeTofile(data, filename
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') __ file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

___ readBlobData(empId
    ___
        sqliteConnection _ ?.c..('SQLite_Python.db')
        cursor _ ?.c..
        print("Connected to SQLite")

        sql_fetch_blob_query _ """S.. _ f.. new_employee w.. id = ?"""
        ?.e..(sql_fetch_blob_query, (empId,))
        record _ ?.f_a..
        ___ row __ record:
            print("Id = ", ? 0], "Name = ", ? 1])
            name  _ ? 1]
            photo _ ? 2]
            resumeFile _ ? 3]

            print("Storing employee image and resume on disk \n")
            photoPath _ "E:\pynative\Python\photos\db_data\\" + name + ".jpg"
            resumePath _ "E:\pynative\Python\photos\db_data\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)

        ?.c..

    _____ ?.E.. __ error:
        print("Failed to read blob data f.. sqlite table" ?
    f..
        __ (?
            ?.c..
            print("sqlite connection is closed")

readBlobData(1)
readBlobData(2)

# Output:
#
# Connected to SQLite
# Id =  1 Name =  Smith
# Storing employee image and resume on disk
#
# Stored blob data into:  E:\pynative\Python\photos\db_data\Smith.jpg
#
# Stored blob data into:  E:\pynative\Python\photos\db_data\Smith_resume.txt
#
# sqlite connection is closed
#
# Connected to SQLite
# Id =  2 Name =  David
# Storing employee image and resume on disk
#
# Stored blob data into:  E:\pynative\Python\photos\db_data\David.jpg
#
# Stored blob data into:  E:\pynative\Python\photos\db_data\David_resume.txt
#
# sqlite connection is closed