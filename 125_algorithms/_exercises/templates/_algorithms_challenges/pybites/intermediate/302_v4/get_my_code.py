# _______ __
# ____ p.. _______ P..
# ____ u__.r.. _______ u..
# _______ j__
#
# filename "my_code.json"
# url "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
# tmp  P.. __.g.. "TMP", "/tmp"
# json_input_file tmp / filename
#
# __ n.. ?.e..
#     u.. ?.f.. f.._f.. ?
#
#
# ___ get_json_data
#     w__ o.. ? __ ?
#         r.. j__.l.. ?
#
#
# json_data ?
#
#
# ___ _make_filename bite
#     """creates a filename, per spec, for input bite (dict)"""
#     r.. ? 'bite' .s.. '.' 0.r.. ' ' '' + '.py'
#
#
# ___ _write_code bite
#     outfile ? / ?
#     ?.w.. ? 'passing_code'
#
#
# ___ get_passing_code json_data_?
#     """
#     Get all passing code and write the code for each bite to
#     individual files. Output file names should be the bite name and
#     number with a .py extension, but not including the description.
#     For example, if the bite name is 'Bite 124. Marvel data analysis'
#     the output file names should be Bite124.py. Remove any/all spaces
#     from the file name.  Write to /tmp (tmp variable).
#     """
#     ___ bite __ ? 'bites' :
#         ? ?
