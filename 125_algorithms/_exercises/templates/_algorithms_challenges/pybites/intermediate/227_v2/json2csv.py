# ____ p.. _______ P..
# _______ c__
# _______ j__
# _______ r__
# ____ j__.d.. _______ J..
#
# EXCEPTION 'exception caught'
# TMP P..('/tmp')
#
#
# ___ convert_to_csv json_file
#     """Read/load the json_file (local file downloaded to /tmp) and
#        convert/write it to defined csv_file.
#         The data is in mounts > collected
#
#        Catch bad JSON (JSONDecodeError) file content, in that case print the defined
#        EXCEPTION string ('exception caught') to stdout reraising the exception.
#        This is to make sure you actually caught this exception.
#
#        Example csv output:
#        creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
#        32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
#        63502,ability_mount_hordescorpionamber,True,...
#        ...
#     """  # noqa E501
#     #csv_file = TMP / json_file.name.replace('.json', '.csv')
#
#     # you code
#
#     ___
#         data j__.l.. ?
#     ______ J..
#         print E..
#         r..
#
#
#     creatures data 'mounts'  'collected'
#
#     field_names l.. ? 0 .k..
#
#
#     w__ o.. c.. _ __ csv_file
#         writer c__.D.. ? f.._f..
#         ?.w..
#
#
#         ___ creature __ ?
#             w__.w.. ?
#
#
#
#
#
#
#
#
#
#
# __ _______ __ _______
#     json_file 'https://bites-data.s3.us-east-2.amazonaws.com/mount-data1.json'
#     convert_to_csv(json_file)
#
#
#
