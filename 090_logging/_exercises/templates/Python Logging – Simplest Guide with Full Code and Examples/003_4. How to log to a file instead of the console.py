# To send the log messages to a file from the root logger, you need to set the file argument in logging.basicConfig()

______ l____
l____.basicConfig(level=l____.INFO, file='sample.log')

# Now all subsequent log messages will go straight to the file sample.log in your current working directory.
# If you want to send it to a file in a different directory, give the full file path.