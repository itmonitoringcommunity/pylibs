import logging
import graypy

def testlog(logger="test-gelf-udp",localhost="192.168.1.106",port=12203,message="test"):
    try:
        my_logger = logging.getLogger(logger)
        my_logger.setLevel(logging.DEBUG)
        handler = graypy.GELFHandler(localhost, port)
        my_logger.addHandler(handler)
        my_logger.debug(message)
    except :
        return False
    return True

def testlog2(logger="test-gelf-udp-2",localhost="192.168.1.106",port=12204,message="test",type="log",description="description"):
    try:
        my_logger = logging.getLogger(logger)
        my_logger.setLevel(logging.DEBUG)
        handler = graypy.GELFHandler(localhost, port)
        my_logger.addHandler(handler)
        
        my_adapter = logging.LoggerAdapter(logging.getLogger(logger),{ 'type': type, 'description':description })
        my_adapter.debug(message)

    except :
        return False
    return True
