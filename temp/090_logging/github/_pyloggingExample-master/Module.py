______ ?

# create logger
module_logger _ ?.gL..('build.log.gingerModule')

class Copy:
    def __init__(self):
        self.logger _ ?.gL..('build.log.gingerModule.Copy')
    def execute(self):
        self.logger.info('COPY')        
        self.logger.info('Sucessfull')


class Delete:
    def __init__(self):
        self.logger _ ?.gL..('build.log.gingerModule.Delete')
    def execute(self):
        self.logger.info('DELETE')        
        self.logger.info('Sucessfull')
