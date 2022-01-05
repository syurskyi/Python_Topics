_______ json

_______ p__

____ jsonify _______ convert_to_json


@p__.f..(scope="module")
___ output
    r.. convert_to_json()


___ test_return_type(output):
    ... t..(output) __ s..


___ test_extracted_data_is_correct(output):
    data = json.loads(output)
    ... t..(data) __ l..
    ... l..(data) __ 10
    ___ row __ [{"id": "1", "first_name": "Junie", "last_name": "Kybert",
                 "email": "jkybert0@army.mil"},
                {"id": "2", "first_name": "Sid", "last_name": "Churching",
                 "email": "schurching1@tumblr.com"},
                {"id": "3", "first_name": "Cherry", "last_name": "Dudbridge",
                 "email": "cdudbridge2@nifty.com"},
                {"id": "4", "first_name": "Merrilee", "last_name": "Kleiser",
                 "email": "mkleiser3@reference.com"},
                {"id": "5", "first_name": "Umeko", "last_name": "Cray",
                 "email": "ucray4@foxnews.com"},
                {"id": "6", "first_name": "Jenifer",
                 "last_name": "Dale", "email": "jdale@hubpages.com"},
                {"id": "7", "first_name": "Deeanne", "last_name": "Gabbett",
                 "email": "dgabbett6@ucoz.com"},
                {"id": "8", "first_name": "Hymie", "last_name": "Valentin",
                 "email": "hvalentin7@blogs.com"},
                {"id": "9", "first_name": "Alphonso", "last_name":
                 "Berwick", "email": "aberwick8@symantec.com"},
                {"id": "10", "first_name": "Wyn", "last_name": "Serginson",
                 "email": "wserginson9@naver.com"}]:
        ... row __ data, f"{row} not in output of convert_to_json"
