______ ____


c_ InvalidSchemeException(E..):
    p..


c_ ConfigurationManager:
    ___  - 
        p..

    ___ get  configuration):
        r_ ____.loads(open(configuration, 'r').read())

    ___ validate  json_str):
        """
        validate input
        raise InvalidSchemeException
        raise json.JSONDecodeError
        :param json_str:
        :return:
        """
        ret _ ____.loads(json_str)
