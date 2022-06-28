import sys
import logging 


class Logger(object):
    level_relations = { 
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射
    
    def __init__(self,filename,level='info'):
        self.logger = logging.getLogger()
        handler = logging.FileHandler(filename)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s]%(message)s",datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(self.level_relations.get(level)) # 设置日志级别        
        
file_log_name = 'log_test.log'
file_log = Logger(file_log_name,level='info').logger

a = 1
file_log.info('a')
file_log.info('b')
file_log.info("数量{}".format(a))

print('af','df')






