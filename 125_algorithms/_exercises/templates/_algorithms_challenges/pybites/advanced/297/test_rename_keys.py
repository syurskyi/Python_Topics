____ d__ _______ d__
_______ p__

____ rename_keys _______ rename_keys


___ fb(value
    r.. s.. ?


?p__.m__.p.('test_input, expected', [
                        ({}, {}),
                        ({'user_name': 'jdoe'}, {'user_name': 'jdoe'}),
                        ({'@user_name': 'jdoe'}, {'user_name': 'jdoe'}),
                        ({'@user_name': 'jdoe', 1: 'one', 2: 'two', '@three': 3},
                         {'user_name': 'jdoe', 1: 'one', 2: 'two', 'three': 3},),
                        ({(T.., F.. '@Fizz@', (F.., T.. '@Buzz@', (T.., T.. '@FizzBizz@', (F.., F.. fb},
                         {(T.., F.. '@Fizz@', (F.., T.. '@Buzz@', (T.., T.. '@FizzBizz@', (F.., F.. fb}),
                        ({'@pii': {'name': {'@first_name': 'Jane', '@last_name': 'Doe'},
                                   '@address': [{'@city': 'London'}, {'city': 'Moscow'}],
                                   '@id': 12345,
                                   '@email': 'jane@example.com'}},
                         {'pii': {'name': {'first_name': 'Jane', 'last_name': 'Doe'},
                                  'address': [{'city': 'London'}, {'city': 'Moscow'}],
                                  'id': 12345,
                                  'email': 'jane@example.com'}}),
                        ({'@contentUrl': 'contentUrl',
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
                                              'tags': {'tag': {'@label': 'label'}}}]}},
                         {'contentUrl': 'contentUrl',
                          'createdAt': d__(2020, 6, 11, 9, 8, 13),
                          'dataAccelerationConfig': {'accelerationEnabled': F..},
                          'defaultViewId': 'defaultViewId',
                          'encryptExtracts': F..,
                          'id': 'id',
                          'name': 'Login',
                          'owner': {'id': 'id', 'name': 'name'},
                          'project': {'id': 'id', 'name': 'name'},
                          'showTabs': T..,
                          'size': 1,
                          'tags': {'tag': {'label': 'label'}},
                          'updatedAt': d__(2020, 7, 20, 6, 41, 34),
                          'views': {'view': [{'contentUrl': 'contentUrl',
                                              'createdAt': '2020-06-11T09:08:13Z',
                                              'id': 'id',
                                              'name': 'name',
                                              'tags': {'tag': {'label': 'label'}},
                                              'updatedAt': '2020-07-20T06:41:34Z',
                                              'viewUrlName': 'Sheet1'},
                                             {'contentUrl': 'contentUrl',
                                              'createdAt': '2020-06-11T09:08:13Z',
                                              'id': 'id',
                                              'name': 'name',
                                              'tags': {'tag': {'label': 'label'}},
                                              'updatedAt': 'updatedAt',
                                              'viewUrlName': 'viewUrlName'}]},
                          'webpageUrl': 'webpageUrl'})
])
___ test_rename_keys(test_input, e..
    snapshot_before r.. (test_input)
    renamed rename_keys(test_input)
    snapshot_after r.. (test_input)

    ... renamed __ e..

    # make sure we're returning a new dict and the original dict was not modified in place
    ... test_input __ n.. renamed
    ... snapshot_before __ snapshot_after __ '@' __ snapshot_before ____ T..
