______ ?

____ . ______ config
____ . ______ module1
____ . ______ module2

logger _ ?.gL..( -n)


___ main():
    ______ ?.config
    ?.config.fileConfig(
        fname_config.log_config_path,
        disable_existing_loggers_False,
        defaults_{"logfilename": config.log_output_path}
    )
    x _ module1.fn()
    y _ module2.fn()
    z _ x + y
    logger.i..(f"z = {z}")
    r_ z


__  -n __ "__main__":
    main()
