# Use JSON or YAML logging configuration
# You can configure your logging system in Python code, but then you need to modify your code whenever you want
# to change the log configuration. Another way to do it is to use a logging configuration file. After Python 2.7,
# you can load logging configuration from a dict. It means you can load the logging configuration from a JSON or YAML
# file. Although you can use the old .ini style logging configuration, it is difficult to read and write.
# Here let me show you the logging configuration examples in JSON and YAML

import os
import json
import logging.config

def setup_logging(
    default_path='logging.json',
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
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
