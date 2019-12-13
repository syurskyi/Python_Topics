# # The FileHandler() and Formatter() classes are used to setup the output file and the format of messages for loggers
# # other than the root logger.Do you remember how we setup the filename and the format of the message in the root logger
# # (inside logging.basicConfig()) earlier? We just specified the filename and format parameters in logging.basicConfig()
# # and all subsequent logs went to that file.However, when you create a separate logger, you need to set them up
# # individually using the logging.FileHandler() and logging.Formatter() objects. A FileHandler is used to make your
# # custom logger to log in to a different file. Likewise, a Formatter is used to change the format of your logged
# # messages.
# #
# ______ l____
#
# # Gets or creates a logger
# logger _ l____.gL_ -n
#
# # set log level
# ?.sL_ l____.W..
#
# # define file handler and set formatter
# file_handler _ l____.FH_ logfile.log
# formatter _ l____.F..  '_ asctime _ : _ levelname _ : _ name _ : _ message _'
# fi__.sF_ f..
#
# # add file handler to logger
# ?.aH_ fi..
#
# # Logs
# ?.d...  'A debug message'
# ?.i... 'An info message'
# ?.w... 'Something is not right.'
# ?.e... 'A Major error has happened.'
# ?.c... 'Fatal error. Cannot continue'
#
# # Notice how we set the formatter on the file_handler and not the logger directly.
# # Assuming the above code is run from the main program, if you look inside the working directory,
# # a file named logfile.log will be created if it doesnt exist and would contain the below messages.
# #
# # #> 2019-02-17 12:40:14,797 : WARNING : __main__ : Something is not right.
# # #> 2019-02-17 12:40:14,798 : ERROR : __main__ : A Major error has happened.
# # #> 2019-02-17 12:40:14,798 : CRITICAL : __main__ : Fatal error. Cannot continue
#
# # Note again, the Formatter is set on the FileHandler object and not directly on the logger. Something you may want to
# # get used to.
