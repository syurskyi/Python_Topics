# # main.py
# ______ ___
#
# # we import our custom importer module
# ______ importer
#
# # import module1.py using our own importer
# module1 = ?.im.._('module1', 'module1_source.py', '.')
#
# # we can see that module1 is in sys.modules
# print('sys says:', ___.m__.g.. 'module1', 'module1 not found'
#
# # and we can now import this module "normally" from other locations
# # such as module2.py
# ______ module2
# _2.he..
#
# # notice how the first time we imported (using import_) module1, it "ran" (printed running module1).
# # but the second time we imported it (in module2) it did not
# # that's because Python recovered module1 from cache, and did not rebuild it
