______ ?

from . ______ config
from . ______ module1
from . ______ module2

logger _ ?.gL..(__name__)


def main():
    ______ ?.config
    ?.config.fileConfig(
        fname_config.log_config_path,
        disable_existing_loggers_False,
        defaults_{"logfilename": config.log_output_path}
    )
    x _ module1.fn()
    y _ module2.fn()
    z _ x + y
    logger.info(f"z = {z}")
    return z


if __name__ == "__main__":
    main()
