from datetime import datetime

from daos import LogFile

class Logger:
    def __init__(self, ml_studies_component: str):
        log_file = LogFile
        log_file += "/" + ml_studies_component

    @classmethod
    def get_logger(cls, ml_studies_component: str):
        return cls(ml_studies_component)

    @staticmethod
    def _build_message(s: str, _type: str, ):
        msg = datetime.now().isoformat().ljust(30)
        msg += _type.ljust(10)
        msg += s.ljust(100) if len(s) <= 100 else s[:97] + '...'
        return msg

    def success(self, message: str):
        message = self._build_message(message, 'SUCCESS')
        print(message)
        LogFile.log(message)

    def info(self, message: str):
        message = self._build_message(message, 'INFO')
        print(message)
        LogFile.log(message)

    def warning(self, message: str):
        message = self._build_message(message, 'WARNING')
        print(message)
        LogFile.log(message)

    def error(self, message: str):
        message = self._build_message(message, 'ERROR')
        print(message)
        LogFile.log(message)
