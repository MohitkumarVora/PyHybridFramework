import logging


def setup_logger(level=logging.INFO):
    # Function to setup a logger; can be called from any module
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler('.\\Logs\\automation.log')
    handler.setFormatter(formatter)

    logger = logging.getLogger('test_logger')
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage:
# logger = setup_logger('my_logger', 'my_logfile.log')
# logger.info('This is an info message')
