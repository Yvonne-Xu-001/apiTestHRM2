# 1导包
import logging
from logging import handlers
#初始化日志器
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {}
EMPID = ""
def init_logger():
    #初始化日志实例
    logger = logging.getLogger()
    # 设置日志的等级
    logger.setLevel(logging.INFO)
    # 初始化处理器
    #初始化控制台处理器
    sh = logging.StreamHandler()
    #初始化文件处理器
    log_path = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(log_path,when='H',interval=1,backupCount=7,encoding='utf-8')
    # 初始化格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
     #将格式器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)