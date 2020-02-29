import pyodbc

CONNSTR = \
'DRIVER={SQL Server};SERVER=mhknbn2kdz.database.windows.net;DATABASE=AdventureWorks2012;UID=sqlfamily;PWD=sqlf@m1ly'

def get_employees():
    connection = pyodbc.connect(CONNSTR)
    query = '''
        SELECT DISTINCT TOP 5 FirstName, LastName 
        FROM Person.Person
        ORDER BY LastName, FirstName;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row.FirstName, row.LastName)
    connection.commit()
    connection.close()

get_employees()
