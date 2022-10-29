def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn  # we do this so we can stack register decorators!

        return inner

    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()

    decorator.register = register
    return decorator


@switcher
def dow():
    print('Invalid day of week')


@dow.register(1)
def dow_1():
    print('Monday')


dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))

dow(1)
dow(2)
dow(100)