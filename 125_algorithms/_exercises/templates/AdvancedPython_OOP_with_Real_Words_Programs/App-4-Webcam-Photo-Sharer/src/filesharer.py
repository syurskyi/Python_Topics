____ filestack _____ Client

c_ FileSharer:

    ___  -    filepath, api_key="INSERT YOUR API KEY HERE"):
        filepath = filepath
        api_key = api_key

    ___ share _
        client = Client(api_key)
        new_filelink = client.upload(filepath=filepath)
        r_ new_filelink.url