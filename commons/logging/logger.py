from datetime import datetime


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    @staticmethod
    def _build_message(s: str, level: str, ):
        msg = datetime.now().isoformat().ljust(30)
        msg += level.ljust(10)
        msg += s
        return msg

    def log(self, message: str, level: str = 'N/A', build_message: bool = True):
        if build_message:
            message = self._build_message(message, level)
        print(message)
        self.log_file.log(message=message)

    def success(self, message: str):
        self.log(message, 'SUCCESS')

    def info(self, message: str):
        self.log(message, 'INFO')

    def warning(self, message: str):
        self.log(message, 'WARNING')

    def error(self, message: str):
        self.log(message, 'ERROR')
