# Calling QCoreApplication.quit() is the same as calling QCoreApplication.exit(0). To quote from the qt docs:
#
# After this function has been called, the application leaves the main event loop and returns from the call to exec().
# The exec() function returns returnCode. If the event loop is not running, this function does nothing. [emphasis added]