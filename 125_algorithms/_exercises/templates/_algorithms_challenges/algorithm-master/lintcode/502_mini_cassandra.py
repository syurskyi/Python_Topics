"""
Definition of Column:
class Column:
    ___ __init__(self, key, value
        self.key = key
        self.value = value
"""


class MiniCassandra:

    storage = {}

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    ___ insert(self, raw_key, column_key, column_value
        __ raw_key not in self.storage:
            self.storage[raw_key] = {}

        self.storage[raw_key][column_key] = Column(column_key, column_value)

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    ___ query(self, raw_key, column_start, column_end
        __ raw_key not in self.storage:
            r_ []

        result = [
            column
            ___ column_key, column in self.storage[raw_key].items()
            __ column_start <= column_key <= column_end
        ]

        r_ sorted(result, key=lambda column: column.key)
