_______ __
____ p.. _______ P..
_______ c__
_______ j__
____ j__.decoder _______ JSONDecodeError

EXCEPTION 'exception caught'
TMP P.. __.g.. "TMP", "/tmp"


___ convert_to_csv(json_file
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    csv_file TMP / json_file.name.r..('.json', '.csv')

    w__ o.. json_file, _ __ f:
        ___
            data j__.l.. f)
            fields data 'mounts'  'collected' [0].k..
            w__ o.. csv_file, 'w') __ csv_fp:
                writer c__.DictWriter(csv_fp, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data 'mounts'  'collected' )
        ______ JSONDecodeError __ e:
            print(EXCEPTION)
            r.. e
