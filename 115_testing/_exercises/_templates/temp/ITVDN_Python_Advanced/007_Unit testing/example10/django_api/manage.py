#!/usr/bin/env python
______ __
______ sys

__ __name__ == '__main__':
    __.environ.s_d_('DJANGO_SETTINGS_MODULE', 'tasks.settings')
    try:
        ____ django.core.management ______ execute_from_command_line
    except ImportError __ exc:
        raise ImportError(
            "Couldn't ______ Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) ____ exc
    execute_from_command_line(sys.argv)
