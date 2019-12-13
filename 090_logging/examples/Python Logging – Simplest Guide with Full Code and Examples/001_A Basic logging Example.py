# Python provides an in-built logging module which is part of the python standard library. So you dont need to install
# anything.
#
# To use logging, all you need to do is setup the basic configuration using logging.basicConfig().
# Actually, this is also optional. We will see about that soon.
#
# Then, instead of print(), you call logging.{level}(message) to show the message in console.
#
import logging
logging.basicConfig(level=logging.INFO)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

logging.info("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(a, b)))
# #> INFO:root:Hypotenuse of 3, 4 is 5.0

# The printed log message has the following default format: {LEVEL}:{LOGGER}:{MESSAGE}.
# In the above case, the level is info, because, I called logging.info().
#
# The logger is called root, because that is the default logger and I did not create a new one, yet.
# But what is a logger anyway?
# A logger is like an entity you can create and configure to log different type and format of messages.
# You can configure a logger that prints to the console and another logger that sends the logs to a file,
# has a different logging level and is specific to a given module. More explanations and examples coming up on this.
# Finally, the message is the string I passed to logging.info().
# Now, what would have happened had you not setup logging.basicConfig(level=logging.INFO)?
# Answer: The log would not have been printed.
# Why?
#
# To know that lets understand the levels of logging.