from commons.logging import log_info, log_success, log_error, log_warning

def test_log_success():
    log_success('This is an test')

def test_log_info():
    log_info('This is an test')
    
def test_log_warning():
    log_warning('This is an test')
    
def test_log_error():
    log_error('This is an test')