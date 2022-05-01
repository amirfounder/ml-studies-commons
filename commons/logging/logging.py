from datetime import datetime

from daos import LogFile


def get_logger(ml_studies_component):
    return Logger(ml_studies_component)


class Logger:
    def __init__(self, ml_studies_component: str):
        self.ml_studies_component = ml_studies_component
        self.path = LogFile.dir_path + '/' + ml_studies_component

    @staticmethod
    def _build_message(s: str, level: str, ):
        msg = datetime.now().isoformat().ljust(30)
        msg += level.ljust(10)
        msg += s.ljust(100) if len(s) <= 100 else s[:97] + '...'
        return msg

    def get_log_file(self):
        self.log_file = LogFile(path=LogFile.last_document_path())
        if self.log_file.exceeds_max_size():
            self.log_file = LogFile()
        return self.log_file

    def log(self, message: str, level: str = None, build_message: bool = True):
        if build_message:
            message = self._build_message(message, level)
        print(message)
        self.get_log_file().log(message)

    def success(self, message: str):
        self.log(message, 'SUCCESS')

    def info(self, message: str):
        self.log(message, 'INFO')

    def warning(self, message: str):
        self.log(message, 'WARNING')

    def error(self, message: str):
        self.log(message, 'ERROR')
