class Logger:
    def __init__(self, log_file='application.log'):
        self.log_file = log_file

    def log(self, message, level='INFO'):
        with open(self.log_file, 'a') as f:
            f.write(f'{level}: {message}\n')

    def info(self, message):
        self.log(message, level='INFO')

    def debug(self, message):
        self.log(message, level='DEBUG')

    def error(self, message):
        self.log(message, level='ERROR')