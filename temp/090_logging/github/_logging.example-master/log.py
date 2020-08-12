______ ?
______ ?.handlers


c_ Log:
    ___  -
        pass

    ___ setup_logging
        formt _ '%(a_t_)s - %(filename)s - %(l..)s - %(m..)s'
        formatter _ ?.F..(formt)

        ch _ ?.SH..
        ch.sL..(?.ERROR)
        ch.sF..(formatter)

        fh _ ?.handlers.RHFH...('./my_app.log')
        fh.sL..(?.D..)
        fh.sF..(formatter)

        logger _ ?.gL..('app_name')
        # logger.setLevel must be lower than setLevel for all other handlers,
        # otherwise it will cut off before reaching the other handlers
        logger.sL..(?.I..)
        logger.aH..(ch)
        logger.aH..(fh)
