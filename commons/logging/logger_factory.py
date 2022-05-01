from daos.internals.files.log_file_factory import LogFileFactory

from commons.logging import Logger


class LoggerFactory:
    @staticmethod
    def get_logger(module: str):
        cls = LogFileFactory.get_log_file(module)
        return Logger(cls)
