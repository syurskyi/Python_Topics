stuff = bytearray()

with open("C:\crap.txt:cmd.exe", "rb") as ads:
    stuff = ads.read()
    print(stuff.__len__())
    ads.close()

with open("C:\Users\kilroy\Downloads\cmd.exe", "wb") as ostream:
    ostream.write(stuff)
    ostream.close()
