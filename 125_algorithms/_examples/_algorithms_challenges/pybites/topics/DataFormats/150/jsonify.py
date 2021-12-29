import json
from typing import DefaultDict

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    data = []
    members_list = members.split()
    for index, member in enumerate(members_list):
        line = member.replace('|',',').replace(';',',').split(',')
        if index == 0:
            col0, col1, col2, col3 = line[0], line[1], line[2], line[3]
        else:
            member_dict = DefaultDict(str)
            member_dict[col0] = line[0]
            member_dict[col1] = line[1]
            member_dict[col2] = line[2]
            member_dict[col3] = line[3]
            data.append(member_dict)
    return json.dumps(data)


print(type(convert_to_json()))

data = json.loads(convert_to_json())