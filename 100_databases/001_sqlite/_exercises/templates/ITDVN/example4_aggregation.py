_____ ?


class RowSet:

    def __init__(self):
        self.rows _ set()

    def step(self, value):
        self.rows.add(value)

    def finalize(self):
        return ';'.join(self.rows)


conn _ ?.c..(':memory:')
?.create_aggregate('row_set', 1, RowSet)

cur _ ?.cursor()
cur.e.. 'C.. T.. users(first_name)')
cur.e..
    """I.. I.. users(first_name)
       V.. ("Dmitry"),
              ("Eugene"),
              ("Viktor"),
              ("Nikita"),
              ("Eugene")
     """
)

cur.e.. 'S.. row_set(first_name) AS result F.. users')
results _ cur.f_a..
print(dict())
