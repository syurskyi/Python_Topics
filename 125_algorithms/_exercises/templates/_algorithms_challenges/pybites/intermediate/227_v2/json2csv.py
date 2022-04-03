____ pathlib _______ Path
_______ csv
_______ json
_______ r__
____ json.decoder _______ JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path('/tmp')


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
    #csv_file = TMP / json_file.name.replace('.json', '.csv')

    # you code

    ___
        data = json.load(json_file)
    ______ JSONDecodeError:
        print(EXCEPTION)
        r..


    creatures = data 'mounts'  'collected'

    field_names = l..(creatures[0].keys

    
    w__ o.. csv_file,'w') __ csv_file:
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()


        ___ creature __ creatures:
            writer.writerow(creature)







    

    
__ _______ __ _______
    json_file = 'https://bites-data.s3.us-east-2.amazonaws.com/mount-data1.json'
    convert_to_csv(json_file)



