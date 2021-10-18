______ json

json_list _ []  # store the converted json data for each line
csv_file _ o..('csv_file.txt', 'r')

___ line __ csv_file.readlines():
    club, city, country _ line.strip().split(',')  # first get rid of the \n and then split with ','
    data _ {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.ap..(data)

csv_file.close()

json_file _ o..('json_file.txt', 'w')
json.dump(json_list, json_file)  # write json data to a file
json_file.close()