_______ c__
____ j__.decoder _______ JSONDecodeError
____ u__.r.. _______ u..

_______ p__

____ json2csv _______ convert_to_csv, EXCEPTION, TMP

mount_data (
    'https://bites-data.s3.us-east-2.amazonaws.com/'
    'mount-data{}.json'
)

mount1_expected [
     'creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
     'itemId', 'name', 'qualityId', 'spellId' ,
     '32158', 'ability_mount_drake_blue', 'False', 'True', 'True', 'False',
     '44178', 'Albino Drake', '4', '60025' ,
     '63502', 'ability_mount_hordescorpionamber', 'True', 'False', 'True',
     'True', '85262', 'Amber Scorpion', '4', '123886' ,
     '24487', 'ability_mount_warhippogryph', 'False', 'True', 'True', 'False',
     '45725', 'Argent Hippogryph', '4', '232412' ,
]

mount2_expected [
     'creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
     'itemId', 'name', 'qualityId', 'spellId' ,
     '71381', 'ability_mount_dragonhawkarmorallliance', 'False', 'True',
     'True', 'False', '98259', 'Armored Blue Dragonhawk', '4', '142478' ,
     '304', 'spell_nature_swiftness', 'True', 'False', 'True', 'True', '0',
     'Felsteed', '1', '5784' ,
     '119386', 'inv_warlockmount', 'False', 'True', 'True', 'False', '0',
     "Netherlord's Chaotic Wrathsteed", '1', '232412' ,
]


?p__.m__.p.("file_no, expected, exception", [
    (1, mount1_expected, F..),
    (2, mount2_expected, F..),
    (3, N.., T..),
])
___ test_json2csv(file_no, e.., exception, capfd
    mount_json TMP / f'mount{file_no}.json'
    mount_csv TMP / f'mount{file_no}.csv'

    u..(mount_data.f..(file_no), mount_json)

    __ exception:
        w__ p__.r..(JSONDecodeError) __ exc:
            convert_to_csv(mount_json)
            ... 'Invalid control character' __ s..(exc)

        # testing you actually caught the exception!
        output ?.r .. 0 .s..
        ... ? __ EXCEPTION
        r..

    convert_to_csv(mount_json)
    w__ o.. mount_csv) __ csv_file:
        a.. l..(c__.reader(csv_file
        ... a.. __ e..