# _______ p.... __ pd
# _______ n.... __ np
#
# movie_excel_file "https://bites-data.s3.us-east-2.amazonaws.com/movies.xlsx"
#
#
# ___ explode df lst_cols fill_value='' preserve_index=F..
#     """Helper found on SO to split pipe (|) separted genres into
#        multiple rows so it becomes easier to group the data -
#        https://stackoverflow.com/a/40449726
#     """
#     __ l.. __ n.. N.. a.. l.. l.. > 0 a.. n..
#        isi.. ? l.. t.. __.n.. ?.S..
#         ? ?
#     idx_cols __.c__.d.. ?
#     lens __ ? 0 .s...l..
#     idx __.r.. __.i__.v.. ?
#     res __.D..
#                 col:__.r.. __ ? .v.. l..
#                 ___ ? __ i..
#                 i.._i..
#              .a.. $$ col:__.c.. __.l.. l..>0 ? .v..
#                             ___ ? __ l..
#     __  l.. __ 0 .a__
#         res ?.a.. __.l.. l..__0 i.. s..=F..
#                   .f.. f..
#     res ?.s..
#     __ n.. p..
#         res ?.r.. d.._T..
#     r.. ?
#
#
# ___ group_by_genre data_?
#     """Takes movies data excel file (movie_excel_file) and loads it
#        into a DataFrame (df).
#
#        Explode genre1|genre2|genre3 into separte rows using the provided
#        "explode" function we found here: https://bit.ly/2Udfkdt
#
#        Filters out '(no genres listed)' and groups the df by genre
#        counting the movies in each genre.
#
#        Return the new df of shape (rows, cols) = (19, 1)
#        sorted by movie count descending.
#     """
#     movies __.r.. ? s.._7 u.._'C:D'
#
#     movies genre  = ?.g__.s...s.. '|'
#
#     ? ? movie genre .e.. genre
#
#     ? ?~?.g__.s...c.. no genres
#
#
#     r.. ?.g__.v__.t.. movie
#
