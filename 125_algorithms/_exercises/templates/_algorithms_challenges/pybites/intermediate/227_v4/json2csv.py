_______ os
____ pathlib _______ Path
_______ csv
_______ json
____ json.decoder _______ JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path(os.getenv("TMP", "/tmp"))


___ convert_to_csv(json_file):
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
    csv_file = TMP / json_file.name.r..('.json', '.csv')

    w__ open(json_file, 'r') __ f:
        try:
            data = json.load(f)
            fields = data['mounts']['collected'][0].k..
            w__ open(csv_file, 'w') __ csv_fp:
                writer = csv.DictWriter(csv_fp, fieldnames=fields)
                writer.writeheader()
                writer.writerows(data['mounts']['collected'])
        except JSONDecodeError __ e:
            print(EXCEPTION)
            r.. e
