# from timeit ______ default_timer
#
# class Timer(object):
#     ___ __init__(self, verbose=False):
#         self.verbose = verbose
#         self.timer = default_timer
#
#     ___ __enter__(self):
#         self.start = default_timer()
#         return self
#
#     ___ __exit__(self, *args):
#         end = default_timer()
#         self.elapsed = end - self.start
#         if self.verbose:
#             print("Time taken to execute function: {}".format(self.elapsed))