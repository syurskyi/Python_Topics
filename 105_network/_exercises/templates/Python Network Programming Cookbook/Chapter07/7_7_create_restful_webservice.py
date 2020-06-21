# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 7
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ____ flask ______ Flask
# app _ Flask(__name__)
#
# @app.route('/<int:num>')
# ___ index(num_1):
#     r_ "Your Python Web Service <hr>Fibonacci("+ st..(num) + "): "+ st..(fibonacci(num))+ "<hr>Square("+ st..(num) + "): "+ st..(square(num))
#
# ___ fibonacci(n):
#     __ n __ 0:
#         r_ 0
#     ____ n __ 1:
#         r_ 1
#     ____
#         r_ fibonacci(n-1) + fibonacci(n-2)
#
#
# ___ square(n):
#     print ("Calculating for the number @" n)
#     r_ n*n
#
# __ _______ __ ______
#     app.run(debug_True)
