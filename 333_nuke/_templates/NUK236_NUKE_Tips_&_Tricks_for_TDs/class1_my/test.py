______  json

# data = {"hello": 5}

path = 'logs/data.log'

# _file = open(path, 'w')
#
# json.dump(data, _file)

_file = open(path, "r")

data = json.load(_file)

print(data)
