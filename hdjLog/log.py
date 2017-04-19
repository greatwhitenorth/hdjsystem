import logging
import tempfile
from logging import DEBUG, WARN, WARNING, INFO, CRITICAL, ERROR

class HdjLogger(object):

    logger = None
    logformat = None
    level = None
    logFileName = None
    handlerNumber = 0

    def __init__(self, logname=None, type='console', level=DEBUG):
        self.logger = logging.getLogger('base')
        self.level = level
        self.logformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if type == 'console':
            self.addConsoleHandler()
        elif type == 'logfile':
            self.addFileHandler(logname)
        else:
            self.addConsoleHandler()


    def addConsoleHandler(self):
        console = logging.StreamHandler()
        console.setLevel(self.level)
        console.setFormatter(self.logformat)
        self.logger.addHandler(console)
        self.handlerNumber += 1

    def addFileHandler(self, logname=None):

        if not logname:
            logname = tempfile.NamedTemporaryFile()
        logfile = logging.FileHandler(logname.name)
        logfile.setLevel(self.level)
        logfile.setFormatter(self.logformat)
        self.logger.addHandler(logfile)
        self.logFileName = logname.name
        self.handlerNumber += 1
