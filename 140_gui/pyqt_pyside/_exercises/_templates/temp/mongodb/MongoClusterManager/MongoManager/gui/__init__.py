___ _import_all_modules():
    """dynamically imports all modules in the package"""
    ______ t__
    ______ os
    global -a
    -a _   # list
    globals_, locals_ _ globals(), locals()

    # dynamically import all the package modules
    ___ filename in os.listdir(__name__):
        # process all python files in directory that don't start with underscore
        # (which also keeps this module from importing itself)
        __ filename[0] !_ '_' and filename.s..('.')[-1] in ('py', 'pyw'):
            modulename _ filename.s..('.')[0]  # filename without extension
            package_module _ '.'.join([__name__, modulename])
            ___
                module _ __import__(package_module, globals_, locals_, [modulename])
            ______:
                t__.print_exc()
                raise
            ___ name in module.__dict__:
                __ not name.startswith('_'):
                    globals_[name] _ module.__dict__[name]
                    -a.ap..(name)


_import_all_modules()
