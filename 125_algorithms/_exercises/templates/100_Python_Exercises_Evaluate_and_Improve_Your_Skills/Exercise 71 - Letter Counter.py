#Count how many a the text file has
______ requests

response _ requests.get("http://www.pythonhow.com/data/universe.txt")
text _ response.text
count_a _ text.count("a")
print(count_a)
