import json


class InvalidSchemeException(Exception):
    pass


class ConfigurationManager:
    def __init__(self):
        pass

    def get(self, configuration):
        return json.loads(open(configuration, 'r').read())

    def validate(self, json_str):
        """
        validate input
        raise InvalidSchemeException
        raise json.JSONDecodeError
        :param json_str:
        :return:
        """
        ret = json.loads(json_str)
