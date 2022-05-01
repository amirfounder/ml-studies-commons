from commons.logging import LoggerFactory

def test():
    t1_logger = LoggerFactory.get_logger('t1')
    t2_logger = LoggerFactory.get_logger('t2')

    t1_logger.info('This is a test')
    t2_logger.error('lol')
