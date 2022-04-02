_______ requests


___ nxapi_show_version
    url = 'https://sbx-nxos-mgmt.cisco.com/ins'
    switchuser = 'admin'
    switchpassword = 'Admin_1234!'

    http_headers = {'Content-type': 'application/json-rpc'}
    payload = [{'jsonrpc': '2.0',
                'method': 'cli',
                'params': {'cmd': 'show version',
                           'version': 1}, 'id': 1}]

    response = requests.post(url, json=payload, headers=http_headers,
                             auth=(switchuser, switchpassword), verify=F..).json()

    version = response 'result'  'body'  'kickstart_ver_str'
    r.. version


__ _____ __ _____
    result = nxapi_show_version()
    print(result)
