"""
In this Bite you are going to decode some Base64 encoded csv data.

This is what the encoded data looks like:

Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK

This data would look like this decoded:

first_name,last_name,credit_card
Keelby,MacCafferky,6393719433329924
Linnell,Clemmett,3555584924093954
Elysha,Meighan,6385795793897106
Katalin,Etherton,3584230011680700
Fina,Pasek,5100136631664687
Ardella,Brazier,201712613653374
Dorthea,Karpinski,30502661251172
Ranna,Duff,3576393056493312
Cinnamon,Kaasman,5442028150808570
Jaclin,Tonge,3549852104724527

Use the base64 module to decode this data and extract the last column of (fake)
credit card numbers returning it as a list (see also the type hints and tests).

We generated the data for this exercise using Mockaroo service,
an excellent service to quickly get realistic fake data.
"""

import base64
import csv

def encode():
    input = """first_name,last_name,credit_card
Keelby,MacCafferky,6393719433329924
Linnell,Clemmett,3555584924093954
Elysha,Meighan,6385795793897106
Katalin,Etherton,3584230011680700
Fina,Pasek,5100136631664687
Ardella,Brazier,201712613653374
Dorthea,Karpinski,30502661251172
Ranna,Duff,3576393056493312
Cinnamon,Kaasman,5442028150808570
Jaclin,Tonge,3549852104724527"""

    test = b'gowno w dupe'
    #result = bytes.decode(input,'ascii')
    result = str.encode(input)
    encoded = base64.b64encode(result)
    print(encoded)

    decoded = base64.b64decode(encoded)
    # print(decoded)???
    print(bytes.decode(decoded, 'ascii'))
    inp = bytes.decode(decoded, 'ascii')
    print(type(inp))
    result = csv.reader(inp.splitlines())
    result = list(result)
    r = result[1:]
    end = []
    for e in r:
        end.append(e[2])
    print(end)


"""
def get_credit_cards(data: bytes) -> List[str]:
    bytes = base64.b64decode(data)
    result = bytes.decode("ascii")
    l = []
    for line in result:
        t = line.split(',')
        l.append(t[2])
    return l
"""
encode()
