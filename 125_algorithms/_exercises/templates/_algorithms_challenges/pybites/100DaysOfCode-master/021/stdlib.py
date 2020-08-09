'''http://stackoverflow.com/questions/22195382/how-to-check-if-a-module-library-package-is-part-of-the-python-standard-library'''
from __future__ ______ unicode_literals, print_function
______ sys
from contextlib ______ contextmanager
from importlib ______ import_module


@contextmanager
___ ignore_site_packages_paths(
    paths = sys.path
    # remove all third-party paths
    # so that only stdlib imports will succeed
    sys.path = list(filter(
        None,
        filter(lambda i: 'site-packages' not in i, sys.path)
    ))
    yield
    sys.path = paths


___ is_std_lib(module
    __ module in sys.builtin_module_names:
        r_ True

    with ignore_site_packages_paths(
        imported_module = sys.modules.pop(module, None)
        try:
            import_module(module)
        except ImportError:
            r_ False
        ____
            r_ True
        finally:
            __ imported_module:
                sys.modules[module] = imported_module
