class MetaSigleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSigleton, cls).__call__(*args, **kwargs)
        return cls._instances

class Logger(metaclass=MetaSigleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)