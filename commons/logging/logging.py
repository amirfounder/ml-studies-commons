from datetime import datetime

from daos import LogFile

class Logger:
    def __init__(self, ml_studies_component: str):
        log_file = LogFile
        log_file.path += "/" + ml_studies_component

    @classmethod
    def get_logger(cls, ml_studies_component: str):
        return cls(ml_studies_component)

    @staticmethod
    def _build_message(s: str, level: str, ):
        msg = datetime.now().isoformat().ljust(30)
        msg += level.ljust(10)
        msg += s.ljust(100) if len(s) <= 100 else s[:97] + '...'
        return msg

    def log(self, message: str, level: str, build_message=True):
        if build_message:
            message = self._build_message(message, level)
        print(message)
        LogFile.log(message)

    def success(self, message: str, build_message=True):
        self.log(message, 'SUCCESS')

    def info(self, message: str):
        self.log(message, 'INFO')

    def warning(self, message: str):
        self.log(message, 'WARNING')

    def error(self, message: str):
        self.log(message, 'ERROR')
