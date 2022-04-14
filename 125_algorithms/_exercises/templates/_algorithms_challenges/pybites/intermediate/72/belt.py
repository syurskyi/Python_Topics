# ____ c.. _______ O..
#
# scores  [10, 50, 100, 175, 250, 400, 600, 800, 1000]
# belts  'white yellow orange green blue brown black paneled red'.s..
#
#
# ___ get_belt user_score scoresscores beltsbelts
#     ninja_belts  O..
#
#     ___ i __ r.. l.. scores
#         ? ? ?  ? ?
#
#     __ user_score < 10:
#         r.. N..
#     ____ ? > 1000:
#         r.. ? 1000
#     ____ user_score > 10 a.. ? < 50
#         r.. ? 10
#     ____ ? > 50 a.. ? < 100
#         r.. ? 50
#     ____ ? > 100 a.. ? < 175
#         r.. ? 100
#     ____ ? > 175 a.. ? < 250
#         r.. ? 175
#     ____ ? > 250 a.. ? < 400
#         r.. ? 250
#     ____ ? > 400 a.. ? < 600
#         r.. ? 400
#     ____ ? > 600 a.. ? < 800
#         r.. ? 600
#     ____ ? > 800 a.. ? < 1000
#         r.. ? 800
#
# # if __name__ == "__main__":
# #     print(get_belt(10002))