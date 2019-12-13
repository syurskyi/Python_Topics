# With the flexibility of the logging module, its a good practice to write logging record everywhere with appropriate
# level and configure them later. What is the appropriate level to use, you may ask. Let me share my experience here.
#
# In most cases, you dont want to flood your log file with too many trivial information. And as the name implies,
# the DEBUG level is for debugging. Therefore, the DEBUG level should only be enabled when you are debugging.
# I use the DEBUG level only for logging verbose details. Especially when the data is huge, or the frequency is high,
# such as records of algorithm internal state changes in a for-loop.
#
def complex_algorithm(items):
    for i, item in enumerate(items):
        # do some complex algorithm computation
        logger.debug('%s iteration, item=%s', i, item)

# I use INFO level for routines. For example, handling requests or server state changed.

def handle_request(request):
    logger.info('Handling request %s', request)
    # handle request here
    result = 'result'
    logger.info('Return result: %s', result)

def start_service():
    logger.info('Starting service at port %s ...', port)
    service.start()
    logger.info('Service is started')

# I use WARNING when something needs your attention, but not an error. For example, when a user attempts to log in
# with a wrong password, or, the connection is slow.
#
def authenticate(user_name, password, ip_address):
    if user_name != USER_NAME and password != PASSWORD:
        logger.warning('Login attempt to %s from IP %s', user_name, ip_address)
        return False
    # do authentication here

# I use ERROR level when something is wrong. For example, an exception is thrown, IO operation failure or connectivity
# issue.
#
# def get_user_by_id(user_id):
#     user = db.read_user(user_id)
#     if user is None:
#         logger.error('Cannot find user with user_id=%s', user_id)
#         return user
#     return user
# I never use CRITICAL, you can use it when something horrible happens. For example, out of memory, the disk is full
# or a nuclear meltdown (Hopefully that will not actually happen ).