import logging

class CustomLogger():
    def __init__(self, name, level, logfile):
        """
        param: name: name of the logger
        param: level: loggin level. Use this format --> logging.INFO, 
        param: logfile: file name to store the logs
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not self.logger.handlers: # to avoid duplicate handlers
            file_handler = logging.FileHandler(filename=logfile, mode="a", encoding="utf-8")
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
    

if __name__ == '__main__':
    my_logger = CustomLogger(__name__, level=logging.DEBUG, logfile="logs.log").get_logger()
    my_logger.info("This is a test log")
