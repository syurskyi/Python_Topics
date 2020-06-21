# #!/usr/bin/env python
# # Python Network Programming Cookbook -- Chapter - 4
# # This program requires Python 3.5.2 or any later version
# # It may run on any other version with/without modifications.
# #
# # Follow the comments inline to make it run on Python 2.7.x.
#
#
# ______ re__
# ______ u__
#
# # Uncomment the below line for Python 2.7.x.
# #import urllib2
#
# ID_USERNAME _ 'signup-user-name'
# ID_EMAIL _ 'signup-user-email'
# ID_PASSWORD _ 'signup-user-password'
# USERNAME _ 'username'
# EMAIL _ 'you@email.com'
# PASSWORD _ 'yourpassword'
# SIGNUP_URL _ 'https://twitter.com/account/create'
#
#
# ___ submit_form
#     """Submit a form"""
#     payload _ {ID_USERNAME : USERNAME,
#                ID_EMAIL    :  EMAIL,
#                ID_PASSWORD : PASSWORD,}
#
#     # make a get request
#     resp _ ?.g.. S_U..
#     print ("Response to GET request: @" ?.c..
#
#     # send POST request
#     resp _ ?.post(SIGNUP_URL, payload)
#     print ("Headers from a POST request response: @" ?.h..
#
#
# __ _______ __ ______
#     ?
#
