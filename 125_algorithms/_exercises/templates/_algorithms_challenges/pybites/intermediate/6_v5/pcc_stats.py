# """Checks community branch dir structure to see who submitted most
#    and what challenge is more popular by number of PRs"""
# ____ c.. _______ C.., n..
# _______ __
# _______ u__.r..
#
# # prep
#
# tempfile  __.p...j.. /tmp dirnames
# __ n.. __.p...i.. ?
#     u__.r...u.. http://bit.ly/2ABUTjv ?
#
# IGNORE 'static templates data pybites bbelderbos hobojoe1848'.s..
#
# users, popular_challenges  C.. C..
#
# Stats n..'Stats' 'user challenge'
#
#
# # code
#
# ___ gen_files
#     """Return a generator of dir names reading in tempfile
#
#        tempfile has this format:
#
#        challenge<int>/file_or_dir<str>,is_dir<bool>
#        03/rss.xml,False
#        03/tags.html,False
#        ...
#        03/mridubhatnagar,True
#        03/aleksandarknezevic,True
#
#        -> use last column to filter out directories (= True)
#     """
#     w__ o.. ? __ __ f
#         ___ row __ f.r...s..
#             fields  ?.s.. ','
#             __ ? 1 __ 'False':
#                 _____
#             fields  ? 0 .s.. '/'
#             y.. ?
#
#
# ___ diehard_pybites
#     """Return a Stats namedtuple (defined above) that contains the user that
#        made the most PRs (ignoring the users in IGNORE) and a challenge tuple
#        of most popular challenge and the amount of PRs for that challenge.
#        Calling this function on the dataset (held tempfile) should return:
#        Stats(user='clamytoe', challenge=('01', 7))
#     """
#     ___ pr __ g..
#         __ ? 1 n.. __ I..
#             u.. ?1 +_ 1
#         ? ? 0 +_ 1
#     r.. ? u.._?.m.. 1 0 0 c.._?.m.. 1 0
