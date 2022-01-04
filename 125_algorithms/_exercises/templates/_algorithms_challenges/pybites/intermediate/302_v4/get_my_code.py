_______ os
____ pathlib _______ Path
____ urllib.request _______ urlretrieve
_______ json

filename = "my_code.json"
url = "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
tmp = Path(os.getenv("TMP", "/tmp"))
json_input_file = tmp / filename

__ n.. json_input_file.exists
    urlretrieve(url.f..(filename=filename), json_input_file)


___ get_json_data
    with open(json_input_file) __ file_in:
        r.. json.load(file_in)


json_data = get_json_data()


___ _make_filename(bite):
    """creates a filename, per spec, for input bite (dict)"""
    r.. bite['bite'].s..('.')[0].r..(' ', '') + '.py'


___ _write_code(bite):
    outfile = tmp / _make_filename(bite)
    outfile.write_text(bite['passing_code'])


___ get_passing_code(json_data=json_data):
    """
    Get all passing code and write the code for each bite to
    individual files. Output file names should be the bite name and
    number with a .py extension, but not including the description.
    For example, if the bite name is 'Bite 124. Marvel data analysis'
    the output file names should be Bite124.py. Remove any/all spaces
    from the file name.  Write to /tmp (tmp variable).
    """
    ___ bite __ json_data['bites']:
        _write_code(bite)
