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
from flask import Flask
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)
    # 注册SQLAlchemy
    db.init_app(app)
    # 创建所有表
    # with app.app_context():
    db.create_all(app=app)  # 将数据放入数据库中
    return app


def register_blueprint(app):
    from app.web import view
    app.register_blueprint(view)
