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
from monitor import logger


def _logger():
    try:
        file_tmp = open('1.txt')
        print(file_tmp)
        logger('user', 'info', '钱扬20180001', 0, 'Open success!')
    except IOError:
        logger('user', 'error', '钱扬20180001', 20240001, IOError)


if __name__ == '__main__':
    _logger()
