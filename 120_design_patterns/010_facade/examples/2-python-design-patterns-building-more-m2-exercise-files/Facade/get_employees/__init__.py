PROVIDER = 'sql_server'

CONNSTR = (
    'DRIVER={SQL Server};'
    'SERVER=mhknbn2kdz.database.windows.net;'
    'DATABASE=AdventureWorks2012;'
    'UID=sqlfamily;PWD=sqlf@m1ly'
)

QUERY = '''
    SELECT DISTINCT TOP 5 FirstName, LastName 
    FROM Person.Person
    ORDER BY LastName, FirstName;
'''