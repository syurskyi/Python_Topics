# # Imports and importlib
# # In the last video we saw how we could, in a simplistic manner, mimic Python's import.
# # There is absolutely no need to do this since Python itself provides that functionality, both as a built-in function
# # (import) and in the standard library module importlib.
# # In fact, if you want to see how imports are done in pure Python code you can always look at the source code for that
# # library (you should now know where to find that on your local machine - you have to first identify
# # a Pythyon environment (sys.exec_prefix) and then look in the lib folder:
# #
# _______ ___
# print ___.e..p_
# #
# # Or you can import importlib and look at the __file__ property to get an exact location:
#
# ______ __l__
# print(importlib. -f
# #
# # or just see the string representation of the importlib object:
#
# print(__l__)
# # <module 'importlib' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\importlib\\__init__.py'>
# #
# # You'll find something a little different - importlib is not actually a pure module (it's still a module type object) -
# # it's actually a package - more on that later.
# # You should then use the import_module function to load a module.
# # For example, we can load the fractions module as follows:
# #
# __l__.i_m. fractions
# # <module 'fractions' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py'>
# #
# # The problem doing it this way is that our module namespace does not have a symbol for fractions (but it is in sys.modules):
# #
# # f = fractions.Fraction(2, 3)
# #
# # ---------------------------------------------------------------------------
# # NameError                                 Traceback (most recent call last)
# # <ipython-input-7-92ac4b49f1a5> in <module>()
# # ----> 1 f = fractions.Fraction(2, 3)
# #
# # NameError: name 'fractions' is not defined
# #
# # So instead we would have to do it the same way we did it with our own custom importer:
#
# fractions = __l__.i_m. fractions
# #
# # And now we have a symbol for the fractions object.
# #
# f = f_.F.. 2 3
# print(f)
# # Fraction(2, 3)
# #
# # One thing I briefly alluded to earlier, we can import from a variety of "sources".
# # Often it is from file, such as with fractions:
#
# print ?
# # <module 'fractions' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py'>
# #
# # Sometimes it is built in to Python directly:
# #
# _______ ma..
# print(ma..
# #
# # <module 'math' (built-in)>
# #
# # In Python there are a number of files that are "code" files, such as
# #     .py: basic text file containing Python code
# #     .pyc: compiled Python code (bytecode)
# #     .so, .pyd: think DLL's (Linux / Windows)
# #
# # amongst others. Furthermore, Python can reach inside zip archives for code (as well as other packaged distribution
# # files such as those used by Egg or Wheel).
# # In very broad terms the import system, once the "source" code has been located works as we saw in the last video.
# # A lot of the complexity comes from locating a module when we try to import it.
# # Conceptually Python divides the work between finders and loaders.
# #
# # The finders are responsible for finding the module/package and returning the module spec, while the loaders,
# # are responsible for "loading" the source code that is then used in the final steps to compile, execute and cache
# # the module object. An object that implements both is called an importer - but they are still two separate concepts.
# # Python provides a number of standard finders and importers, such as:
# #     built-in modules
# #     frozen modules
# #     import path finder (finds source code files on the import path - for example the sys.path entries we have seen
# #     before)
# # What's interesting about the import path finder and loader is that they can search (and load from) zip archives.
# # In fact it can even be extended to search other resources, including url's, databases, etc.
# # You could theoretically store code in a Mongo or Redis database and import directly from there!
# # Let's look at the module spec for fractions:
# #
# print(fr__. -s
# # ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B83757F0>, origin='D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py')
# #
# # As you can see the finder determined where the source code was located, and also indicated that the loader
# # to be used is the SourceFileLoader.
# # How does Python know which finder to use in the first place?
# # It doesn't really - it will go through a bunch of finders, one by one, until one returns a module spec -
# # if it exhausts all the registered finders and finds nothing, then we get the module not found exception:
# #
# # import foo
# #
# # ---------------------------------------------------------------------------
# # ModuleNotFoundError                       Traceback (most recent call last)
# # <ipython-input-15-34d390fb3acc> in <module>()
# # ----> 1 import foo
# #
# # ModuleNotFoundError: No module named 'foo'
# #
# # Here are the finders currently registered on my system:
# #
# print ___.me..
# #
# # [_frozen_importlib.BuiltinImporter,
# #  _frozen_importlib.FrozenImporter,
# #  _frozen_importlib_external.PathFinder,
# #  <six._SixMetaPathImporter at 0x154b64d0198>,
# #  <pkg_resources.extern.VendorImporter at 0x154b7148f98>,
# #  <pkg_resources._vendor.six._SixMetaPathImporter at 0x154b72a5518>]
# #
# # When we import our custom file-based modules, the PathFinder will be used to find the file.
# # We can also use importlib to find the spec for a particular module:
# #
# __l__.u__.f_s.  math
# # ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
# #
# __l__.u__.f_s. fractions
# # ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B83757F0>, origin='D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py')
# #
# # Let's write out a small source file to disk, called module1.py:
# # with open('module1.py', 'w') as code_file:
# #     code_file.write("print('running module1.py...')\n")
# #     code_file.write('a = 100\n')
# #
# # Now that we have the module on disk, we can ask importlib for the module spec:
# #
# __l__.u__.f_s. module1
# #
# # ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B8435390>, origin='d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Modules, Packages and Namespaces\\04 - Imports and importlib\\module1.py')
# #
# # As you can see, it found the file and indicated it would be imported using the SourceFileLoader.
# # Now let's go ahead and actually import it:
# #
# ________ module1
# # running module1.py...
# #
# print(?.a)
# # 100
# #
# # Now let's go ahead and write a file somewhere other than our source folder - you'll have to change this code
# # to specify your path where you want that module file to be created:
# #
# ________ __
#
# # you can use this for Mac/Linux:
# # ext_module_path = os.environ['HOME']
#
# # you can use this in Windows 10
# #ext_module_path = os.environ['HOMEPATH']
#
# # or you can just hard code some path
# # ext_module_path = 'c:\\temp'
#
# ext_module_path = __.e___.g.. HOME __.e.. HOMEPATH
#
# print ?
#
# # '\\Users\\fbapt'
# #
# _______ __
# file_abs_path _ __.pa__.j.. ? module2.py
# w___ o.. ? _ __ code_file
#     ?.w..("print('running module2.py...')\n")
#     ?.w..("x = 'python'\n")
#
# # Let's see if Python can figure the module spec:
# #
# ___l__.u__.f_s.. module2
# #
# # Nothing came back - it was not able to locate that module anywhere...
# #
# _______ module2
# #
# # ---------------------------------------------------------------------------
# # ModuleNotFoundError                       Traceback (most recent call last)
# # <ipython-input-27-4fbab195dd19> in <module>()
# # ----> 1 import module2
# #
# # ModuleNotFoundError: No module named 'module2'
# # As expected, the import failed.
# # By the way, you can use try...except for your imports!
# #
# t___
#     _______ ?
# e____ M...
#     # could not find module
#     # maybe import an alternative module instead??
#     # e.g. import module1 as module2
#     # but please do not just silence the exception!
#     # if you're importing the module most likely you are
#     # using it somewhere in your code - so raise an
#     # exception at the precise location where the root cause
#     # occurred!
#     # so the following is BAD!!
#     print('Module was not found.')
#
# # Module was not found.
# # The module was not found because sys.path knows nothing about ext_module_path.
#
# print e... __ ___.pa..
# # False
# #
# # So, let's add it!
# #
# print ___.pa__.ap.. e...
# #
# # Now let's try finding the module spec again:
# #
# _____l__.u__.f_s.. module2
# # ModuleSpec(name='module2', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B84356A0>, origin='\\Users\\fbapt\\module2.py')
# #
# # Hurray! Our import should now work...
# #
# _______ module2
# # running module2.py...
# #
# print(?.x)
# #
# # 'python'
# #
# # We can "hack" the sys.path list by adding our own entries directly - but this means we would have to hard code
# # these paths in our code, or potentially read them from a configuration file.
# # It's perfectly fine to do that, but you may prefer using .pth files for that.
# # I'm not going to get into the details of this - the Python docs are located here: