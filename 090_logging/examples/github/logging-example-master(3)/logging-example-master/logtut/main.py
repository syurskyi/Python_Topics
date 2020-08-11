import logging

from . import config
from . import module1
from . import module2

logger = logging.getLogger(__name__)


def main():
    import logging.config
    logging.config.fileConfig(
        fname=config.log_config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": config.log_output_path}
    )
    x = module1.fn()
    y = module2.fn()
    z = x + y
    logger.info(f"z = {z}")
    return z


if __name__ == "__main__":
    main()
