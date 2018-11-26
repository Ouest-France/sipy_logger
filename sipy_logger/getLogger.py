
import logging, os
import graypy
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

def getLogger(name='logger', localLoggingLevel=logging.INFO, messageFormat='%(asctime)-15s %(levelname)s %(message)s', messagePrefix=None,
    # file logging (time-based rotation)
    fileDir=None, filename=None,
    # size-based file rotation (size in bytes, mx number >=1)
    rotatingFileMaxSize=None, rotatingFileMaxNumber=None,
    # graylog logging
    graylog=None, graylogLoggingLevel=logging.INFO
):
    """Returns a logger configured with the given characteristics"""

    # returns the named logger if it already has defined handlers (avoids double logging when getLogger is called several times with the same logger name)
    logger = logging.getLogger(name)
    if logger.handlers and len(logger.handlers) > 0:
        return logger

    # sets max sensitivity so that it catches all log calls (the handlers will filter them)
    logger.setLevel(logging.DEBUG)
    # avoids double-logging by the root logger (https://docs.python.org/3.6/library/logging.html#logging.Logger.propagate)
    logger.propagate = False

    # common formatter
    formatter = logging.Formatter(
        '{} {}'.format(('' if messagePrefix is None else messagePrefix), messageFormat).strip()
    )

    # terminal handler
    terminalHandler = logging.StreamHandler()
    terminalHandler.setLevel(localLoggingLevel)
    terminalHandler.setFormatter(formatter)
    logger.addHandler(terminalHandler)

    # optional file handler (directory must exist)
    if fileDir is not None and os.path.isdir(fileDir):
        filePath =  os.path.join(fileDir, filename)

        # size-based file rotation
        if rotatingFileMaxSize is not None and rotatingFileMaxNumber is not None:
            fileHandler = RotatingFileHandler(filePath, 'a', rotatingFileMaxSize, rotatingFileMaxNumber)
        # time-based file rotation
        else:
            fileHandler = TimedRotatingFileHandler(filePath, when='d', interval=1)

        fileHandler.setLevel(localLoggingLevel)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    # optional graylog handler
    if graylog is not None:
        gelfHandler = graypy.GELFHandler(graylog['remoteHost'], graylog['port'])
        gelfHandler.setLevel(graylogLoggingLevel)
        gelfHandler.setFormatter(formatter)
        logger.addHandler(gelfHandler)

    return logger

