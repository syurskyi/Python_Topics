_______ __
____ p.. _______ P..
____ u__.r.. _______ u..
_______ j__

filename "my_code.json"
url "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
tmp  P..(__.g..("TMP", "/tmp"
json_input_file tmp / filename

__ n.. json_input_file.exists
    u..(url.f..(filename=filename), json_input_file)


___ get_json_data
    w__ o.. json_input_file) __ file_in:
        r.. j__.l.. file_in)


json_data get_json_data()


___ get_passing_code(json_data=json_data
    """Get all passing code and write the code for each bite to individual files.
       Output file names should be the bite name and number with a .py extension,
       but not including the description.  For example, if the bite name is
       'Bite 124. Marvel data analysis' the output file name should be Bite124.py.
       Remove any/all spaces from the file name.
       Write to /tmp (tmp variable).
    """
    ___ row __ json_data["bites"]:
        filename_pre row["bite"].s..(".")[0].r..(" ", "")
        w__ o.. f"{tmp}/{filename_pre}.py", "w") __ f:
            f.w.. row["passing_code"])


# if __name__ == "__main__":
#     get_passing_code()