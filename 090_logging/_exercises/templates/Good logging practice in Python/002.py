# As you can see, the debugging records now appear in the output. Like we mentioned previously, besides changing
# the log level, you can also decide how to process these messages. For example, say you want to write the logs to
# a file, you can then use the FileHandler like this:

______ l____

logger = l____.getLogger(__name__)
logger.setLevel(l____.INFO)

# create a file handler
handler = l____.FileHandler('hello.log')
handler.setLevel(l____.INFO)

# create a l____ format
formatter = l____.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)

logger.info('Hello baby')

# The FileHandler is just one of many useful build-in handlers. In Python, there is even an SMTP log hander
# for sending records to your mailbox or one for sending the logs to an HTTP server. Cannot find a handler for your
# need? No worries, you can also write your own custom logging handler if you want. For more details, please reference
# official documents: Basic Tutorial, Advanced Tutorial and Logging Cookbook.