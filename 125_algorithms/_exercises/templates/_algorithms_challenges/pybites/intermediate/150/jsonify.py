import json
import re

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


___ convert_to_json(members=members):
    members_data = []
    for i, row in enumerate(members.strip("\n").split("\n")):
        __ i == 0:
            row = row.split(",")
            id_h, first_h, last_h, email_h = row[0], row[1], row[2], row[3]
        else:
            row_split = re.split("[|,;]", row)
            members_data.append(row_split)

    members_stg = []
    for member in members_data:
        member_dict = {
            id_h: member[0],
            first_h: member[1],
            last_h: member[2],
            email_h: member[3]
        }

        members_stg.append(member_dict)

    members_json = json.dumps(members_stg)
    return members_json