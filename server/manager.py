# ------------------------------------------------------------
#  产品：****
#  版本：0.1
#  版权：****
#  模块：****
#  功能：****
#  语言：Python3.6
#  作者：钱扬<sjtu_qianyang@outlook.com>
#  日期：2019-01-21
# ------------------------------------------------------------
#  修改人：钱扬<sjtu_qianyang@outlook.com>
#  修改日期：2019-01-21
#  修改内容：创建
# ------------------------------------------------------------
from app import create_app
from app.secure import ENVIRONMENT

app = create_app()

if __name__ == '__main__':
    if ENVIRONMENT is 'producer':
        app.run(host='0.0.0.0', port=8080, debug=app.config['DEBUG'])
    else:
        app.run(port=8080, debug=app.config['DEBUG'])
