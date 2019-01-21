# ------------------------------------------------------------
#  产品：****
#  版本：0.1
#  版权：****
#  模块：****
#  功能：****
#  语言：Python3.6
#  作者：钱扬<sjtu_qianyang@outlook.com>
#  日期：2018-07-18
# ------------------------------------------------------------
#  修改人：钱扬<sjtu_qianyang@outlook.com>
#  修改日期：2018-07-18
#  修改内容：创建
# ------------------------------------------------------------
import logging
import inspect
from logging.handlers import RotatingFileHandler
import os
from monitor.logger.setting import LOG_DICT
from app.setting import PROJECT_NAME


def __create_logger(module):
    log_name = LOG_DICT[module]['log_name']
    msg_fmt = '[%(levelname)s][%(asctime)s]%(message)s'
    date_fmt = '%Y_%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt=msg_fmt, datefmt=date_fmt)
    _rt_handler = RotatingFileHandler(log_name, maxBytes=20 * 1024 * 1024, backupCount=5)
    _rt_handler.setFormatter(formatter)
    logger_ = logging.getLogger(module)
    if len(logger_.handlers) < 1:
        logger_.addHandler(_rt_handler)
    logger_.setLevel(LOG_DICT[module]['log_level'])
    return logger_


def __get_module_path(file_path):
    module_path = [PROJECT_NAME]
    filename = os.path.basename(file_path).split('.py')
    dir_path = os.path.dirname(file_path).split(PROJECT_NAME)[-1][1:]
    if '\\' in dir_path:
        module_path.extend(dir_path.split('\\'))
    elif '\'' in dir_path:
        module_path.extend(dir_path.split('\''))
    else:
        module_path.extend(dir_path.split('/'))
    module_path.extend(filename)
    module_path = [path_ for path_ in module_path if path_]
    return '.'.join(module_path)


def __log_message(module_name, line_no, func_name, author, code, message):
    return '[{} line:{} {}][{}][{}]{}'.format(module_name, line_no, func_name, author, code, message)


def __log_writer(logger_, level, msg):
    if level is 'critical':
        logger_.critical(msg)
    elif level is 'error':
        logger_.error(msg)
    elif level is 'warning':
        logger_.warning(msg)
    elif level is 'info':
        logger_.info(msg)
    else:
        logger_.debug(msg)


def logger(module, level, author, code, message):
    try:
        logger_ = __create_logger(module)
    except KeyError:
        logger_ = __create_logger('other')
        logger_.error('ModuleInputError!')
    call_stack = inspect.stack()[1]
    module_name = __get_module_path(call_stack[1])
    func_name = call_stack[3]
    line_no = call_stack[2]
    msg = __log_message(module_name, line_no, func_name, author, code, message)
    __log_writer(logger_, level, msg)
    return True
