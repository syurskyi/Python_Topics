# Shell variables os.environ
# Running programs os.system, os.popen, os.execv, os.spawnv
# Spawning processes os.fork, os.pipe, os.waitpid, os.kill
# Descriptor files, locks os.open, os.read, os.write
# File processing os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
# Administrative tools os.getcwd, os.chdir, os.chmod, os.getpid, os.listdir, os.access
# Portability tools os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
# Pathname tools os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')

import os
print(dir(os))

print(dir(os.path))

print(dir(os.system))

print(dir(os.kill))