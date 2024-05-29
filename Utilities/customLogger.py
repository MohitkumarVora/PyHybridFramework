import logging
import os

class LogGen:
    @staticmethod
    def loggen(log_level=logging.INFO):
        logger = logging.getLogger("automationLogger")

        # Check if the logger already has handlers to prevent duplicate logs
        if not logger.hasHandlers():
            log_directory = ".\\Logs"
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            logging.basicConfig(filename=os.path.join(log_directory, "automation.log"),
                                format='%(asctime)s: %(levelname)s: %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p',
                                level=log_level)

            # Creating a console handler for output to the console
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_handler.setFormatter(
                logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
            logger.addHandler(console_handler)

        logger.setLevel(log_level)
        return logger
