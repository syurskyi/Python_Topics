_____ json
_____ ?


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
# cur.execute('S.. * FROM test')
# row = cur.fetchone()
#
# conn.close()


?.register_adapter(dict, adapt_json)
?.register_converter('json', convert_json)

conn _ ?.c..(':memory:', detect_types_?.PARSE_DECLTYPES)
cur _ ?.cursor()

cur.e.. 'C.. T.. test(p json)')
cur.e.. 'I.. I.. test(p) V.. (?)', ({'test': 1, 'ppp': 10},))
cur.e.. 'I.. I.. test(p) V.. (?)', ({'test': 2, 'ppp': 11},))
cur.e.. 'S.. _ F.. test')
record _ cur.fetchone()
print(type(record[0]))
