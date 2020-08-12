import os
import pathlib

src_dir = pathlib.Path(__file__).parent.absolute()
log_config_path = os.path.join(src_dir, "logging.ini")
log_output_path = os.path.join(src_dir, "log.log")
