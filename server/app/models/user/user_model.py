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
from app.models import db
from sqlalchemy import Column, Integer, String


class ToasterMasterUser(db.Model):
    __tablename__ = 'toastermaster_user'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(String(30), nullable=False, primary_key=True)
    user_name = Column(String(30), nullable=False)
    avatar_url = Column(String(1000), nullable=False)
    gender = Column(Integer, nullable=False)
    birthday = Column(String(30), nullable=False)
    country = Column(String(30), nullable=False)
    province = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    club_name = Column(String(30), nullable=False)
    edu_title = Column(String(30), nullable=False)
    user_right = Column(String(30), nullable=False)

    def __init__(self, session):
        self.user_id = str(session['user_id'])
        self.user_name = str(session['user_name'])
        self.avatar_url = str(session['avatar_url'])
        self.gender = int(session['gender'])
        self.birthday = str(session['birthday'])
        self.country = str(session['country'])
        self.province = str(session['province'])
        self.city = str(session['city'])
        self.club_name = str(session['club_name'])
        self.edu_title = str(session['edu_title'])
        self.user_right = str(session['user_right'])


class UserDataModel:
    def __init__(self):
        self.user_id = '__none_id__'
        self.user_name = '__none_name__'
        self.avatar_url = '__none_url__'
        self.gender = -1
        self.birthday = '1800-01-01'
        self.country = 'China'
        self.province = 'Shanghai'
        self.city = 'Shanghai'
        self.club_name = 'AmazingFriday'
        self.edu_title = 'Member'
        self.user_right = 'user'

    def set(self, form):
        self.user_id = str(form['user_id']) if 'user_id' in form else self.user_id
        self.user_name = str(form['user_name']) if 'user_name' in form else self.user_name
        self.avatar_url = str(form['avatar_url']) if 'avatar_url' in form else self.avatar_url
        self.gender = int(form['gender']) if 'gender' in form else self.gender
        self.birthday = str(form['birthday']) if 'birthday' in form else self.birthday
        self.country = str(form['country']) if 'country' in form else self.country
        self.province = str(form['province']) if 'province' in form else self.province
        self.city = str(form['city']) if 'city' in form else self.city
        self.club_name = str(form['club_name']) if 'club_name' in form else self.club_name
        self.edu_title = str(form['edu_title']) if 'edu_title' in form else self.edu_title
        self.user_right = str(form['user_right']) if 'user_right' in form else self.user_right

    def update(self, key, value):
        str_format = '{0}.{1} = {2}'.format(self, key, value)
        eval(str_format)
