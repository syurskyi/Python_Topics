#Get the file in the attachment and produce the printed output
_______ json
____ pprint _______ pprint

with open("company1.json","r") as file:
    d  json.load(file)

#d = json.load("company1.json")

pprint(d)
