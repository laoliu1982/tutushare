import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='mylog.log',filemode='a')

logging.debug('log debug')
logging.info('this is info')
logging.warning('warging')


