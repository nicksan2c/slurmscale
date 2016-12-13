"""Library setup."""
import logging
from logging import NullHandler  # Python 2.7+ only

from util import Config

# Current version of the library
__version__ = '0.1.0'

config = Config()


def get_version():
    """
    Return a string with the current version of the library.

    :rtype: ``string``
    :return:  Library version (e.g., "0.1.0").
    """
    return __version__


#
# ~ Library logging setup
#
# By default, do not force any logging by the library. If you want to see the
# log messages in your scripts, add the following to the top of your script:
#   import slurmscale
#   slurmscale.set_stream_logger(__name__)
#   OR
#   slurmscale.set_file_logger(__name__, '/tmp/ss.log')

TRACE = 5  # Lower than debug, which is 10


class SSLogger(logging.Logger):
    """
    A custom logger, adds logging level below debug.

    Add a ``trace`` log level, numeric value 5: ``log.trace("Log message")``
    """

    def trace(self, msg, *args, **kwargs):
        """Add ``trace`` log level."""
        self.log(TRACE, msg, *args, **kwargs)

default_format_string = "%(asctime)s %(levelname)s %(name)s: %(message)s"
logging.setLoggerClass(SSLogger)
logging.addLevelName(TRACE, "TRACE")
log = logging.getLogger('slurmscale')
log.addHandler(NullHandler())


def set_stream_logger(name, level=TRACE, format_string=None):
    """A convenience method to set the global logger to stream."""
    global log
    if not format_string:
        format_string = default_format_string
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    log = logger


def set_file_logger(name, filepath, level=logging.INFO, format_string=None):
    """A convenience method to set the global logger to a file."""
    global log
    if not format_string:
        format_string = default_format_string
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.FileHandler(filepath)
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    log = logger
