___ _import_all_modules():
    """dynamically imports all modules in the package"""
    _______ traceback
    _______ os
    global __all__
    __all__ = []
    globals_, locals_ = globals(), locals()

    # dynamically import all the package modules
    ___ filename __ os.listdir(__name__):
        # process all python files in directory that don't start with underscore
        # (which also keeps this module from importing itself)
        __ filename[0] != '_' and filename.split('.')[-1] __ ('py', 'pyw'):
            modulename = filename.split('.')[0]  # filename without extension
            package_module = '.'.join([__name__, modulename])
            ___
                module = __import__(package_module, globals_, locals_, [modulename])
            ______
                traceback.print_exc()
                raise
            ___ name __ module.__dict__:
                __ not name.startswith('_'):
                    globals_[name] = module.__dict__[name]
                    __all__.append(name)


_import_all_modules()
