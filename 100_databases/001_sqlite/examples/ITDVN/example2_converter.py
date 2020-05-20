import json
import sqlite3


def adapt_json(data):
	return json.dumps(data)


def convert_json(raw):
	return json.loads(raw)


# conn = sqlite3.connect(":memory:")
# cur = conn.cursor()
#
# cur.execute('CREATE TABLE test(p json)')
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 3, 'ppp': 12},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 4, 'ppp': 13},))
# cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 5, 'ppp': 14},))
# cur.execute('SELECT * FROM test')
# row = cur.fetchone()
#
# conn.close()


sqlite3.register_adapter(dict, adapt_json)
sqlite3.register_converter('json', convert_json)

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

cur.execute('CREATE TABLE test(p json)')
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 1, 'ppp': 10},))
cur.execute('INSERT INTO test(p) VALUES (?)', ({'test': 2, 'ppp': 11},))
cur.execute('SELECT * FROM test')
record = cur.fetchone()
print(type(record[0]))
