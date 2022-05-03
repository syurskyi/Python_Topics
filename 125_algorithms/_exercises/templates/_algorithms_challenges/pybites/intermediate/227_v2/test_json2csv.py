# _______ c__
# ____ j__.d.. _______ J..
# ____ u__.r.. _______ u..
#
# _______ p__
#
# ____ ? _______ ? ? ?
#
# mount_data
#     'https://bites-data.s3.us-east-2.amazonaws.com/'
#     'mount-data{}.json'
#
#
# mount1_expected
#      'creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
#      'itemId', 'name', 'qualityId', 'spellId' ,
#      '32158', 'ability_mount_drake_blue', 'False', 'True', 'True', 'False',
#      '44178', 'Albino Drake', '4', '60025' ,
#      '63502', 'ability_mount_hordescorpionamber', 'True', 'False', 'True',
#      'True', '85262', 'Amber Scorpion', '4', '123886' ,
#      '24487', 'ability_mount_warhippogryph', 'False', 'True', 'True', 'False',
#      '45725', 'Argent Hippogryph', '4', '232412' ,
#
#
# mount2_expected
#      'creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
#      'itemId', 'name', 'qualityId', 'spellId' ,
#      '71381', 'ability_mount_dragonhawkarmorallliance', 'False', 'True',
#      'True', 'False', '98259', 'Armored Blue Dragonhawk', '4', '142478' ,
#      '304', 'spell_nature_swiftness', 'True', 'False', 'True', 'True', '0',
#      'Felsteed', '1', '5784' ,
#      '119386', 'inv_warlockmount', 'False', 'True', 'True', 'False', '0',
#      "Netherlord's Chaotic Wrathsteed", '1', '232412' ,
# ]
#
# ?p__.m__.p. "file_no, expected, exception", [
#     (1, ? F..),
#     (2, ? F..),
#     (3, N.., T..),
#
# ___ test_json2csv file_no e.. exception capfd
#     mount_json ? / _*mount f__ .json
#     mount_csv ? / _*mount f__ .csv
#
#     u.. m__.f.. f.. m..
#
#     __ exception
#         w__ p__.r.. J... __ exc
#             ? ?
#             ... 'Invalid control character' __ s.. ?
#
#         # testing you actually caught the exception!
#         output ?.r .. 0 .s..
#         ... ? __ E..
#         r..
#
#     ? ?
#     w__ o.. m.. __ c..
#         a.. l.. c__.r.. c..
#         ... a.. __ e..
