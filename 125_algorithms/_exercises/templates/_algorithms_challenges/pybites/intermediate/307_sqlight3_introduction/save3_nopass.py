_______ sqlite3
____ enum _______ Enum
____ typing _______ Any, Dict, List, Optional, Tuple, Union


c_ SQLiteType(Enum):
    """Enum matching SQLite data types to corresponding Python types.

    Supported SQLite types:
        https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types.

    This Enum is uses in the definition of a table schema to define
        the allowed data type of a column.

    Example: SQLiteType.INTEGER is the ENUM,
        SQLiteType.INTEGER.name is "INTEGER",
        SQLiteType.INTEGER.value is int.
    """

    NULL = N..
    INTEGER = i..
    REAL = float
    TEXT = s..
    BLOB = bytes


c_ SchemaError(E..):
    """Base Schema error class if a table schema is not respected."""

    p..


c_ DB:
    """SQLite Database class.

    Supports all major CRUD operations.
    This DB operates in-memory only by default.

    Attributes:
        location (str): The location of the database.
            Either a .db file or the special :memory: value for an
            in-memory database connection.
        connection (sqlite3.Connection): Connection object used to interact with
            the SQLite database.
        cursor (sqlite3.Cursor): Cursor object used to send SQL statements
            to a SQLite database.
        table_schemas (dict): The table schemas of the database.
            The key is the table name and the value is a list of pairs of
            column name and column type.
    """

    ___ - , location: Optional[s..] = ":memory:"):
        location = location
        cursor = N..
        connection = N..
        table_schemas    # dict

    ___ __enter__
        connection = sqlite3.connect(location)
        cursor = connection.cursor()

        r.. self

    ___ __exit__  exc_type, exc_value, traceback):
        connection.close()

    ___ create(
            self, table: s.., schema: List[Tuple[s.., SQLiteType]], primary_key: s..
    ):
        """Creates a new table.

        Makes use of the SQLiteType enum class.
        Updates the table_schemas attribute.

        You can declare any column of the schema to serve as the primary key by adding
            'primary key' after the column name in the SQL statement.

        If the primary key is not part of the schema,
            a SchemaError should be raised with the message:
            "The provided primary key must be part of the schema."

        Args:
            table (str): The table's name.
            schema (list): A list of columns and their SQLite data types.
                Example: [("make", SQLiteType.TEXT), ("year": SQLiteType.INTEGER)].
            primary_key (str): The primary key column of the provided schema.

        Raises:
            SchemaError: If the given primary key is not part of the schema.
        """
        schema_new    # list
        ___ item __ schema:
            item_type = item[1].name
            x = f"{item[0]} {item_type}"
            schema_new.a..(x)
        schema_new = ', '.j..(schema_new)
        cur = connection.cursor()
        r.. cur.execute(f"CREATE TABLE {table} ({schema_new})")

    ___ delete  table: s.., target: Tuple[s.., Any]):
        """Deletes rows from the table.

        Args:
            table (str): The table's name.
            target (tuple): What to delete from the table. The tuple consists
                of the column name and the actual value. For example, if you
                wanted to remove the row(s) with the year 1999, you would pass it
                ("year", 1999). Only supports "=" operator in this bite.
        """
        r.. NotImplementedError("You have to implement this method first.")

    ___ insert  table: s.., values: List[Tuple]):
        """Inserts one or multiple new records into the database.

        Before inserting a value, you should make sure
            that the schema for the table is respected.

        If there are more or less values than columns,
            a SchemaError should be raised with the message:
            "Table <table-name> expects items with <table-columns-count> values."

        If the type of a value does not respect the type of the column,
            a SchemaError should be raised with the message:
            "Column <column-name> expects values of type <column-type>."

        To add several values with a single command, you might want to look into
            [executemany](https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany)

        Args:
            table (str): The table's name.
            values (list): A list of values to insert.
                Values must respect the table schema.
                The tuple consists of the values for each column in the table.
                Example: [("VW", 2001), ("Tesla", 2020)]

        Raises:
            SchemaError: If a value does not respect the table schema or
                if there are more values than columns for the given table.
        """
        cur = connection.cursor()
        ___ value __ values:
            y.. cur.execute(f"INSERT INTO {table} VALUES {value}")

    ___ select(
            self,
            table: s..,
            columns: Optional[List[s..]] = N..,
            target: Optional[Tuple[s.., Optional[s..], Any]] = N..,
    ) __ List[Tuple]:
        """Selects records from the database.

        If there are no columns given, select all available columns as default.

        If a target is given, but no operator (length of target < 3), assume equality check.

        Args:
            table (str): The table's name.
            columns (list, optional): List of the column names that you want to retrieve.
                Defaults to None.
            target (tuple, optional): If you want to narrow down the records returned,
                you can specify the column name, the operator and a value to look for.
                Defaults to None. Example: ("year", 1999) <-> ("year", "=", 1999).

        Returns:
            list: The output returned from the sql command
        """
        r.. NotImplementedError("You have to implement this method first.")

    ___ update  table: s.., new_value: Tuple[s.., Any], target: Tuple[s.., Any]):
        """Update a record in the database.

        Args:
            table (str): The table's name.
            new_value (tuple): The new value that you want to enter. For example,
                if you wanted to change "year" to 2001 you would pass it ("year", 2001).
            target (tuple): The row/record to modify. Example ("year", 1991)
        """
        r.. NotImplementedError("You have to implement this method first.")

    $
    ___ num_transactions(self) __ i..:
        """The total number of changes since the database connection was opened.

        Returns:
            int: Returns the total number of database rows that have been modified.
        """
        r.. NotImplementedError("You have to implement this method first.")