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
import os

from app.secure import ENVIRONMENT

_LOG_LEVEL_DICT = {'developer': logging.DEBUG, 'producer': logging.INFO}
_LOG_LEVEL_DEV = logging.DEBUG
_LOG_LEVEL_PRO = logging.INFO
_FILE_DIR_DICT = {'developer': os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                  'producer': os.path.dirname(os.path.dirname(__file__))}
_LOG_DIR = os.path.join(_FILE_DIR_DICT[ENVIRONMENT], 'log')
if not os.path.exists(_LOG_DIR):
    os.makedirs(_LOG_DIR)
LOG_DICT = {
    'meeting': {'log_name': os.path.join(_LOG_DIR, 'toaster_meeting_book.log'),
                'log_level': _LOG_LEVEL_DICT[ENVIRONMENT]},
    'user': {'log_name': os.path.join(_LOG_DIR, 'toaster_user.log'),
             'log_level': _LOG_LEVEL_DICT[ENVIRONMENT]}
}