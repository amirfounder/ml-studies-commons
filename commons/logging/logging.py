from datetime import datetime

from daos import (
    ErrorLogFile,
    WarningLogFile,
    InfoLogFile,
    SuccessLogFile
)

def build_message(s: str, _type: str):
    msg = datetime.now().isoformat().ljust(30)
    msg += _type.ljust(10)
    msg += s.ljust(100) if len(s) <= 100 else s[:97] + '...'
    return msg


def log_success(message: str):
    message = build_message(message, 'SUCCESS')
    print(message)
    SuccessLogFile.log(message)

def log_info(message: str):
    message = build_message(message, 'INFO')
    print(message)
    InfoLogFile.log(message)

def log_warning(message: str):
    message = build_message(message, 'WARNING')
    print(message)
    WarningLogFile.log(message)

def log_error(message: str):
    message = build_message(message, 'ERROR')
    print(message)
    ErrorLogFile.log(message)
