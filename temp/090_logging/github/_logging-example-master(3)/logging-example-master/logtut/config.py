______ os
______ pathlib

src_dir _ pathlib.Path(__file__).parent.absolute()
log_config_path _ os.path.join(src_dir, "logging.ini")
log_output_path _ os.path.join(src_dir, "log.log")
