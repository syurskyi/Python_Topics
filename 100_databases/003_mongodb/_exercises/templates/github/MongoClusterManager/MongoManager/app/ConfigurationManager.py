_______ json


c_ InvalidSchemeException(Exception):
    pass


c_ ConfigurationManager:
    ___  -
        pass

    ___ get(self, configuration):
        return json.loads(open(configuration, 'r').read())

    ___ validate(self, json_str):
        """
        validate input
        raise InvalidSchemeException
        raise json.JSONDecodeError
        :param json_str:
        :return:
        """
        ret = json.loads(json_str)
