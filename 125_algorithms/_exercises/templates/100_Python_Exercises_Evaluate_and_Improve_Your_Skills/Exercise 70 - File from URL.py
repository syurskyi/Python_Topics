#Print out the text of this file www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.
______ requests

response _ requests.get("http://www.pythonhow.com/data/universe.txt")
text _ response.text
print(text)
