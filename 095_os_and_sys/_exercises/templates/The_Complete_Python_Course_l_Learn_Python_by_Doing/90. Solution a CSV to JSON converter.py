import json

json_list = []  # store the converted json data for each line
csv_file = open('csv_file.txt', 'r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')  # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)  # write json data to a file
json_file.close()