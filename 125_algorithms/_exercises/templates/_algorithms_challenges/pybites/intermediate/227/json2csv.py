# _______ __
# ____ p.. _______ P..
# _______ c__
# _______ j__
# ____ j__.d.. _______ J..
#
# EXCEPTION 'exception caught'
# TMP P.. __.g.. "TMP", "/tmp"
#
#
# ___ convert_to_csv json_file
#    """Read/load the json_file (local file downloaded to /tmp) and
#       convert/write it to defined csv_file.
#        The data is in mounts > collected
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
#    """  # noqa E501
#    csv_file T.. / ?.n__.r.. '.json', '.csv'
#
#    # you code
#    w__ o.. ? __ f
#       ___
#          data j__.l.. ?.r..
#       ______ J..
#          print E..
#          r..
#
#    mounts d.. "mounts" "collected"
#    w__ o.. c.. _ __ f
#       headers key ___ ? __ ? 0 .k..
#       writer c__.D.. ? f.._?
#
#       ?.w..
#       ___ row __ mounts
#          w__.w.. ?
#
