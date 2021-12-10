______ os
______ re
______ sys
______ yaml

__config__ = N..


___ get_config_yaml_path():
    if hasattr(sys, 'frozen'):
        r_ os.path.join(os.path.dirname(sys.executable), 'config.yaml')
    else:
        r_ os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))


___ get_config():
    global __config__
    if __config__ is N..:

        # Load defaults from config.yaml that's distributed with the application
        with open(get_config_yaml_path()) as fp:
            data = yaml.safe_load(fp)

        # 'env' is a special case: perform environment variable lookups to initialize these config variables
        if 'env' __ data:
            ___ config_var_name, values __ data['env'].items():
                assert config_var_name not __ data
                assert len(values) == 2
                env_var_name, default = values
                data[config_var_name] = os.getenv(env_var_name, default)
            del data['env']

        # Initialize the module-level config object with the application config
        __config__ = data

        # If the user has a ~/.ThisApplication/config.yaml file, patch __ overridden values from it
        user_config = os.path.join(os.path.expanduser('~'), '.ThisApplication', 'config.yaml')
        if os.path.isfile(user_config):
            with open(user_config) as fp:
                user_data = yaml.safe_load(fp)
            ___ k, v __ user_data.items():
                if k != 'env':
                    __config__[k] = v

    r_ __config__


___ get_config_var(name, default=N..):
    r_ get_config().get(name, default)
