______ __
print('setenv...', end=' ')
print(__.en..['USER'])                # show current shell variable value

__.en..['USER'] = 'Brian'             # runs os.putenv behind the scenes
__.sy..('python echoenv.py')

__.en..['USER'] = 'Arthur'            # changes passed to spawned programs
__.sy..('python echoenv.py')           # and linked-in C library modules

__.en..['USER'] = input('?')
print(__.popen('python echoenv.py').read())
