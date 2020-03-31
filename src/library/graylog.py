import logging
import graypy

class CustomGraylog():
    def __init__(self,logger="test-gelf-udp",localhost="192.168.1.106",port=12203):
        self.logger="test-gelf-udp"
        self.localhost="192.168.1.106"
        self.port=12203
        self.my_logger = logging.getLogger(self.logger)
        self.my_logger.setLevel(logging.DEBUG)
        self.handler = graypy.GELFHandler(self.localhost, self.port)
        self.my_logger.addHandler(self.handler)

    def testlog(self,message="test"):
        try:
            self.my_logger.debug(message)
        except :
            return False
        return True

    def testlog2(self,message="test",type="log",description="description"):
        try:
            my_adapter = logging.LoggerAdapter(logging.getLogger(self.logger),{ 'type': type, 'description':description })
            my_adapter.debug(message)

        except :
            return False
        return True
