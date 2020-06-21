# # One advantage of using JSON configuration is that Python has json as a standard library, unlike YAML, you dont need
# # to install a third-party library. But personally, I prefer YAML. Its clear to read and easier to write.
# # You can install PyYAML and load the YAML configuration with the following recipe:
# #
# ______ os
# ______ l____.c..
# 
# ______ yaml
# 
# ___ setup_logging(
#     default_path_'l____.yaml',
#     default_level_l____.I..,
#     env_key='LOG_CFG'
# ):
#     """Setup logging configuration
# 
#     """
#     path _ d..
#     value _ __.g_e_ e.. N..
#     i_ v..
#         p.. _ v..
#     i_ __.pa...ex.. pa..
#         w__ o... p.. __ a_ f
#             config = y___.s._l. ?.re..
#         l____.c__.dC_ c..
#     e__
#         l____.bC_ le.._d..
# 
# # Now, to setup l____, you can call setup_logging when starting your program. It reads l____.json or l____.yaml
# # by default. You can also set LOG_CFG environment variable to load the l____ configuration from a path. For example,
# #
# # LOG_CFG=my_logging.json python my_server.py
# # or if you prefer YAML
# #
# # LOG_CFG=my_logging.yaml python my_server.py
