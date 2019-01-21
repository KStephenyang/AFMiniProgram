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
from flask import request, abort, jsonify
from app.controller.user.user_controller import user_control
from app.validation.user.user_val import UserForm
from . import view


@view.route('/toastermaster/user/baseinfo', methods=['GET', 'POST'])
def user_baseinfo():
    form = UserForm(request.json)
    if form.validate():
        return jsonify(user_control(request.json)), 201
    else:
        abort(404)


@view.route('/toastermaster/user/login', methods=['GET', 'POST'])
def user_login():
    form = UserForm(request.json)
    if form.validate():
        return jsonify(user_control(request.json)), 201
    else:
        abort(404)


@view.route('/toastermaster/meeting/book', methods=['GET', 'POST'])
def meeting_book():
    form = UserForm(request.json)
    if form.validate():
        return jsonify(user_control(request.json)), 201
    else:
        abort(404)
