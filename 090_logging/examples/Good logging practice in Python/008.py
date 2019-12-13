# One advantage of using JSON configuration is that Python has json as a standard library, unlike YAML, you dont need
# to install a third-party library. But personally, I prefer YAML. Its clear to read and easier to write.
# You can install PyYAML and load the YAML configuration with the following recipe:
#
import os
import logging.config

import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# Now, to setup logging, you can call setup_logging when starting your program. It reads logging.json or logging.yaml
# by default. You can also set LOG_CFG environment variable to load the logging configuration from a path. For example,
#
# LOG_CFG=my_logging.json python my_server.py
# or if you prefer YAML
#
# LOG_CFG=my_logging.yaml python my_server.py