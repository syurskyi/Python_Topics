_______ json
_______ __

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


___ convert_to_json(members=members
    members_data    # list
    ___ i, row __ e..(members.strip("\n").s..("\n":
        __ i __ 0:
            row = row.s..(",")
            id_h, first_h, last_h, email_h = row[0], row[1], row[2], row[3]
        ____:
            row_split = __.s..("[|,;]", row)
            members_data.a..(row_split)

    members_stg    # list
    ___ member __ members_data:
        member_dict = {
            id_h: member[0],
            first_h: member[1],
            last_h: member[2],
            email_h: member[3]
        }

        members_stg.a..(member_dict)

    members_json = json.dumps(members_stg)
    r.. members_json