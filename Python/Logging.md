Logging
=======

Minimum working example
-----------------------
~~~
import logging
import sys

def main():
    logging.basicConfig(
            format='%(asctime)s %(message)s',
            datefmt='%Y%d%m %I:%M:%S %p', filename=app_name+'.log')
    logging.debug('here we are in debug')
    logging.info('this is "info"')
    logging.warn('we are warned herewith')
    logging.error('this tests the use of "logging.error" rather than our own '
            'logger')
    logging.critical('couldn\'t be worse')

if __name__ == '__main__':
    main()
~~~


My current model (20130404)
---------------------------

~~~
import logging
import sys

def main(logging_flag):
    # Set the logging level; default choices:
    # DEBUG, INFO, WARN, ERROR, CRITICAL
    log_levels = {
            '-d': logging.DEBUG,
            '-i': logging.INFO,
            '-e': logging.ERROR,
            '-c': logging.CRITICAL}
    # WARN is default.
    if logging_flag in log_levels:
        the_level = log_levels[logging_flag]
    else:
        the_level = logging.WARN
    #
    # Set the application name and logger configuration.
    # We don't want the .py extension.
    app_name = __file__.split('.')[0]
    logging.basicConfig(
            format='%(asctime)s (' + app_name + '.%(funcName)s:%(lineno)d) '
                '%(levelname)s: %(message)s',
            datefmt=%Y%d%m_%H:%M:%S_%Z',
            filename=app_name+'.log',
            level=the_level)
    #
    # The following are sample logging messages.
    logging.debug('here we are in debug')
    logging.info('this is "info"')
    logging.warn('we are warned herewith')
    logging.error('this tests the use of "logging.error" rather than our own '
            'logger')
    logging.critical('couldn\'t be worse')

if __name__ == '__main__':
    # Only the last flag on the command line is noticed.
    main(sys.argv[-1])
~~~


Attributes for formatting log entries
-------------------------------------

http://docs.python.org/3.2/library/logging.html#logrecord-attributes, accessed 20130404.
