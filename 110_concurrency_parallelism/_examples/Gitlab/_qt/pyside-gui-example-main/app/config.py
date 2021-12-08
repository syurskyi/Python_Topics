import os
import re
import sys
import yaml

__config__ = None


def get_config_yaml_path():
    if hasattr(sys, 'frozen'):
        return os.path.join(os.path.dirname(sys.executable), 'config.yaml')
    else:
        return os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))


def get_config():
    global __config__
    if __config__ is None:

        # Load defaults from config.yaml that's distributed with the application
        with open(get_config_yaml_path()) as fp:
            data = yaml.safe_load(fp)

        # 'env' is a special case: perform environment variable lookups to initialize these config variables
        if 'env' in data:
            for config_var_name, values in data['env'].items():
                assert config_var_name not in data
                assert len(values) == 2
                env_var_name, default = values
                data[config_var_name] = os.getenv(env_var_name, default)
            del data['env']

        # Initialize the module-level config object with the application config
        __config__ = data

        # If the user has a ~/.ThisApplication/config.yaml file, patch in overridden values from it
        user_config = os.path.join(os.path.expanduser('~'), '.ThisApplication', 'config.yaml')
        if os.path.isfile(user_config):
            with open(user_config) as fp:
                user_data = yaml.safe_load(fp)
            for k, v in user_data.items():
                if k != 'env':
                    __config__[k] = v

    return __config__


def get_config_var(name, default=None):
    return get_config().get(name, default)
