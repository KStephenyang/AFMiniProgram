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


class UserForm:
    def __init__(self, request_json):
        self.request_json = request_json
        self.robot_id = None
        self.user_id = None

    def validate(self):
        if not self.request_json:
            return False
        self.robot_id = self.request_json["robot_id"] if "robot_id" in self.request_json else None
        self.user_id = self.request_json["user_id"] if "user_id" in self.request_json else None
        if self.robot_id and self.user_id:
            return True
        else:
            return False
