# One advantage of using JSON configuration is that Python has json as a standard library, unlike YAML, you dont need
# to install a third-party library. But personally, I prefer YAML. Its clear to read and easier to write.
# You can install PyYAML and load the YAML configuration with the following recipe:
#
______ os
______ l____.config

______ yaml

def setup_logging(
    default_path='l____.yaml',
    default_level=l____.INFO,
    env_key='LOG_CFG'
):
    """Setup l____ configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        l____.config.dictConfig(config)
    else:
        l____.basicConfig(level=default_level)

# Now, to setup l____, you can call setup_logging when starting your program. It reads l____.json or l____.yaml
# by default. You can also set LOG_CFG environment variable to load the l____ configuration from a path. For example,
#
# LOG_CFG=my_logging.json python my_server.py
# or if you prefer YAML
#
# LOG_CFG=my_logging.yaml python my_server.py