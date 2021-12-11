______ os
______ re
______ sys
______ yaml

__config__ = N..


___ get_config_yaml_path():
    __ hasattr(sys, 'frozen'):
        r_ os.path.join(os.path.dirname(sys.executable), 'config.yaml')
    ____
        r_ os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config.yaml'))


___ get_config():
    g.. __config__
    __ __config__ __ N..:

        # Load defaults from config.yaml that's distributed with the application
        w__ o..(get_config_yaml_path()) __ fp:
            data = yaml.safe_load(fp)

        # 'env' is a special case: perform environment variable lookups to initialize these config variables
        __ 'env' __ data:
            ___ config_var_name, values __ data['env'].items():
                assert config_var_name n.. __ data
                assert l..(values) == 2
                env_var_name, default = values
                data[config_var_name] = os.getenv(env_var_name, default)
            del data['env']

        # Initialize the module-level config object with the application config
        __config__ = data

        # If the user has a ~/.ThisApplication/config.yaml file, patch __ overridden values from it
        user_config = os.path.join(os.path.expanduser('~'), '.ThisApplication', 'config.yaml')
        __ os.path.isfile(user_config):
            w__ o..(user_config) __ fp:
                user_data = yaml.safe_load(fp)
            ___ k, v __ user_data.items():
                __ k != 'env':
                    __config__[k] = v

    r_ __config__


___ get_config_var(name, default=N..):
    r_ get_config().get(name, default)
