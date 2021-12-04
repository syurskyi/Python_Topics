import json

with open("file2.txt") as json_file1:
    data = json.load(json_file1)
print("DATA", data)

data["metals"]["gold"] = {
    "conductivity": 33.5,
    "density": 0.255,
    "heat": 0.129,
    "melting point": 2171,
    "thermal expansion": 4.7,
    "yield strength": 288,
    "tensile strength": 441,
    "minimum impact energy": 22
    }
with open("file2.txt", "w") as json_file2:
    json.dump(data, json_file2)