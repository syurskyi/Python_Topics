____ typing _______ Dict, Any
____ datetime _______ datetime

_______ re


___ rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:


    new_dict = {}


    ___ key,value __ data.items():


        __ isi..(key,str):
            key = re.sub(r'^@','',key)

        __ isi..(value,d..):
            new_dict[key] = rename_keys(value)
        ____:
            __ isi..(value,l..):
                values    # list
                ___ v __ value:
                    values.a..(rename_keys(v))
                value = values
            new_dict[key] = value



        

    r.. new_dict



__ __name__ __ "__main__":



    d = {'@contentUrl': 'contentUrl',
         '@createdAt': datetime.strptime('2020-06-11T09:08:13Z', '%Y-%m-%dT%H:%M:%SZ'),
          '@defaultViewId': 'defaultViewId',
          '@encryptExtracts': False,
          '@id': 'id',
          '@name': 'Login',
          '@showTabs': True,
          '@size': 1,
          '@updatedAt': datetime.strptime('2020-07-20T06:41:34Z', '%Y-%m-%dT%H:%M:%SZ'),
          '@webpageUrl': 'webpageUrl',
          'dataAccelerationConfig': {'@accelerationEnabled': False},
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


    print(rename_keys(d))
