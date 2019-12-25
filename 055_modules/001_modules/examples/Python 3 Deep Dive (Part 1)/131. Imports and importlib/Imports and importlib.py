# %%
'''
### Imports and `importlib`
'''

# %%
'''
In the last video we saw how we could, in a simplistic manner, mimic Python's import.
There is absolutely no need to do this since Python itself provides that functionality, both as a built-in function 
(`import`) and in the standard library module `importlib`.
In fact, if you want to see how imports are done in pure Python code you can always look at the source code for that 
library (you should now know where to find that on your local machine - you have to first identify a Pythyon environment 
(`sys.exec_prefix`) and then look in the `lib` folder:
'''

# %%
import sys

# %%
print(sys.exec_prefix)

# %%
'''
Or you can import `importlib` and look at the `__file__` property to get an exact location:
'''

# %%
import importlib

# %%
print(importlib.__file__)

# %%
'''
or just see the string representation of the `importlib` object:
'''

# %%
importlib

# %%
'''
You'll find something a little different - `importlib` is not actually a pure module (it's still a module type object) 
- it's actually a package - more on that later.
'''

# %%
'''
You should then use the `import_module` function to load a module.
'''

# %%
'''
For example, we can load the `fractions` module as follows:
'''

# %%
importlib.import_module('fractions')

# %%
'''
The problem doing it this way is that **our** module namespace does not have a symbol for `fractions` 
(but it **is** in `sys.modules`):
'''

# %%
f = fractions.Fraction(2, 3)

# %%
'''
So instead we would have to do it the same way we did it with our own custom importer:
'''

# %%
fractions = importlib.import_module('fractions')

# %%
'''
And now we have a symbol for the `fractions` object.
'''

# %%
f = fractions.Fraction(2, 3)

# %%
f

# %%
'''
One thing I briefly alluded to earlier, we can import from a variety of "sources".

Often it is from file, such as with `fractions`:
'''

# %%
fractions

# %%
'''
Sometimes it is built in to Python directly:
'''

# %%
import math

# %%
math

# %%
'''
In Python there are a number of files that are "code" files, such as

* `.py`: basic text file containing Python code
* `.pyc`: compiled Python code (bytecode)
* `.so`, `.pyd`: think DLL's (Linux / Windows)

amongst others. Furthermore, Python can reach inside `zip` archives for code (as well as other packaged distribution
files such as those used by Egg or Wheel).
'''

# %%
'''
In very broad terms the import system, once the "source" code has been located works as we saw in the last video.
A lot of the complexity comes from locating a module when we try to import it.
'''

# %%
'''
Conceptually Python divides the work between **finders** and **loaders**.
The **finders** are responsible for finding the module/package and returning the module spec, while the **loaders**,
 are responsible for "loading" the source code that is then used in the final steps to compile, execute and cache 
 the module object. An object that implements both is called an **importer** - but they are still two separate concepts.
'''

# %%
'''
Python provides a number of standard finders and importers, such as:

* built-in modules
* frozen modules
* import path finder (finds source code files on the import path - for example the `sys.path` entries we have seen 
before)
What's interesting about the import path finder and loader is that they can search (and load from) zip archives.
In fact it can even be extended to search other resources, including url's, databases, etc. You could theoretically 
store code in a Mongo or Redis database and import directly from there!
'''

# %%
'''
Let's look at the module spec for `fractions`:
'''

# %%
print(fractions.__spec__)

# %%
'''
As you can see the finder determined where the source code was located, and also indicated that the loader to be used 
is the SourceFileLoader.
How does Python know which finder to use in the first place?
It doesn't really - it will go through a bunch of finders, one by one, until one returns a module spec - if it exhausts 
all the registered finders and finds nothing, then we get the module not found exception:
'''

# %%
import foo

# %%
'''
Here are the finders currently registered on my system:
'''

# %%
print(sys.meta_path)

# %%
'''
When we import our custom file-based modules, the `PathFinder` will be used to find the file.
'''

# %%
'''
We can also use `importlib` to find the spec for a particular module:
'''

# %%
importlib.util.find_spec('math')

# %%
importlib.util.find_spec('fractions')

# %%
'''
Let's write out a small source file to disk, called module1.py:
'''

# %%
with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write('a = 100\n')

# %%
'''
Now that we have the module on disk, we can ask `importlib` for the module spec:
'''

# %%
importlib.util.find_spec('module1')

# %%
'''
As you can see, it found the file and indicated it would be imported using the SourceFileLoader.
'''

# %%
'''
Now let's go ahead and actually import it:
'''

# %%
import module1

# %%
print(module1.a)

# %%
'''
Now let's go ahead and write a file somewhere other than our source folder - you'll have to change this code 
to specify your path where you want that module file to be created:
'''

# %%
import os

# you can use this for Mac/Linux:
# ext_module_path = os.environ['HOME']

# you can use this in Windows 10
#ext_module_path = os.environ['HOMEPATH']

# or you can just hard code some path
# ext_module_path = 'c:\\temp' 

ext_module_path = os.environ.get('HOME', os.environ['HOMEPATH'])

# %%
print(ext_module_path)

# %%
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")

# %%
'''
Let's see if Python can figure the module spec:
'''

# %%
importlib.util.find_spec('module2')

# %%
'''
Nothing came back - it was not able to locate that module anywhere...
'''

# %%
import module2

# %%
'''
As expected, the import failed.
'''

# %%
'''
By the way, you can use `try...except` for your imports!
'''

# %%
try:
    import module2
except ModuleNotFoundError:
    # could not find module
    # maybe import an alternative module instead??
    # e.g. import module1 as module2
    # but please do not just silence the exception!
    # if you're importing the module most likely you are
    # using it somewhere in your code - so raise an 
    # exception at the precise location where the root cause
    # occurred!
    # so the following is BAD!!
    print('Module was not found.')

# %%
'''
The module was not found because `sys.path` knows nothing about `ext_module_path`.
'''

# %%
print(ext_module_path in sys.path)

# %%
'''
So, let's add it!
'''

# %%
sys.path.append(ext_module_path)

# %%
'''
Now let's try finding the module spec again:
'''

# %%
importlib.util.find_spec('module2')

# %%
'''
Hurray! Our import should now work...
'''

# %%
import module2

# %%
print(module2.x)

# %%
'''
We can "hack" the `sys.path` list by adding our own entries directly - but this means we would have to hard code these 
paths in our code, or potentially read them from a configuration file.
It's perfectly fine to do that, but you may prefer using `.pth` files for that.
I'm not going to get into the details of this - the Python docs are located here:
https://docs.python.org/3/library/site.html
'''