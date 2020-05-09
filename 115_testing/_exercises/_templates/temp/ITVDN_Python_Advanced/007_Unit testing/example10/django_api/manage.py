#!/usr/bin/env python
______ os
______ sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')
    try:
        ____ django.core.management ______ execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't ______ Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) ____ exc
    execute_from_command_line(sys.argv)
