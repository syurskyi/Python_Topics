______ __
print('setenv...', end=' ')
print(__.environ['USER'])                # show current shell variable value

__.environ['USER'] = 'Brian'             # runs os.putenv behind the scenes
__.system('python echoenv.py')

__.environ['USER'] = 'Arthur'            # changes passed to spawned programs
__.system('python echoenv.py')           # and linked-in C library modules

__.environ['USER'] = input('?')
print(__.popen('python echoenv.py').read())
