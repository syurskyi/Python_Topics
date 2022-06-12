____ t___ _______ D.., A..
____ d__ _______ d__

_______ __


___ rename_keys(data: D.. A.., A..]) __ D.. A.., A..]:


    new_dict    # dict


    ___ key,value __ data.i..


        __ isi..(key,s..
            key __.s.. _ ^@','',key)

        __ isi..(value,d..
            new_dict[key] rename_keys(value)
        ____
            __ isi..(value,l..
                values    # list
                ___ v __ value:
                    values.a..(rename_keys(v
                value values
            new_dict[key] value



        

    r.. new_dict



__ _______ __ _______



    d {'@contentUrl': 'contentUrl',
         '@createdAt': d__.s..('2020-06-11T09:08:13Z', '_Y-%m-%dT_H|%M:%SZ'),
          '@defaultViewId': 'defaultViewId',
          '@encryptExtracts': F..,
          '@id': 'id',
          '@name': 'Login',
          '@showTabs': T..,
          '@size': 1,
          '@updatedAt': d__.s..('2020-07-20T06:41:34Z', '_Y-%m-%dT_H|%M:%SZ'),
          '@webpageUrl': 'webpageUrl',
          'dataAccelerationConfig': {'@accelerationEnabled': F..},
          'owner': {'@id': 'id', '@name': 'name'},
          'project': {'@id': 'id', '@name': 'name'},
          'tags': {'tag': {'@label': 'label'}},
          'views': {'view': [{'@contentUrl': 'contentUrl',
                             '@createdAt': '2020-06-11T09:08:13Z',
                              '@id': 'id',
                              '@name': 'name',
                              '@updatedAt': '2020-07-20T06:41:34Z',
                              '@viewUrlName': 'Sheet1',
                              'tags': {'tag': {'@label': 'label'}}},
                             {'@contentUrl': 'contentUrl',
                              '@createdAt': '2020-06-11T09:08:13Z',
                              '@id': 'id',
                              '@name': 'name',
                              '@updatedAt': 'updatedAt',
                              '@viewUrlName': 'viewUrlName',
                                      'tags': {'tag': {'@label': 'label'}}}]}}

    print(d)


    print(rename_keys(d
