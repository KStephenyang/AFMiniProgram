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


class ToasterMasterMeeting(db.Model):
    __tablename__ = 'toastermaster_meeting'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    club_name = Column(String(300), nullable=False, primary_key=True)
    meeting_datetime = Column(String(100), nullable=False)
    monthly_theme = Column(String(100), nullable=False)
    saa = Column(String(100), nullable=False)
    tme = Column(String(100), nullable=False)
    ge = Column(String(100), nullable=False)
    ah_counter = Column(String(100), nullable=False)
    grammarian = Column(String(100), nullable=False)
    timer = Column(String(100), nullable=False)
    ttm = Column(String(100), nullable=False)
    table_topics_theme = Column(String(100), nullable=False)
    speaker_one = Column(String(100), nullable=False)
    speaker_one_speech_project = Column(String(300), nullable=False)
    speaker_one_speech_title = Column(String(300), nullable=False)
    speaker_two = Column(String(100), nullable=False)
    speaker_two_speech_project = Column(String(300), nullable=False)
    speaker_two_speech_title = Column(String(300), nullable=False)
    speaker_three = Column(String(100), nullable=False)
    speaker_three_speech_project = Column(String(300), nullable=False)
    speaker_three_speech_title = Column(String(300), nullable=False)
    speaker_four = Column(String(100), nullable=False)
    speaker_four_speech_project = Column(String(300), nullable=False)
    speaker_four_speech_title = Column(String(300), nullable=False)
    ie_one = Column(String(100), nullable=False)
    ie_two = Column(String(100), nullable=False)
    ie_three = Column(String(100), nullable=False)
    ie_four = Column(String(100), nullable=False)
    sharing_master = Column(String(100), nullable=False)
    sharing_topic = Column(String(300), nullable=False)

    def __init__(self, session):
        self.club_name = str(session['club_name'])
        self.meeting_datetime = str(session['meeting_date'])
        self.monthly_theme = str(session['monthly_theme'])
        self.saa = str(session['saa'])
        self.tme = str(session['tme'])
        self.ge = str(session['ge'])
        self.ah_counter = str(session['ah_counter'])
        self.grammarian = str(session['grammarian'])
        self.timer = str(session['timer'])
        self.ttm = str(session['ttm'])
        self.table_topics_theme = str(session['table_topics_theme'])
        self.speaker_one = str(session['speaker_one'])
        self.speaker_one_speech_project = str(session['speaker_one_speech_project'])
        self.speaker_one_speech_title = str(session['speaker_one_speech_title'])
        self.speaker_two = str(session['speaker_two'])
        self.speaker_two_speech_project = str(session['speaker_two_speech_project'])
        self.speaker_two_speech_title = str(session['speaker_two_speech_title'])
        self.speaker_three = str(session['speaker_three'])
        self.speaker_three_speech_project = str(session['speaker_three_speech_project'])
        self.speaker_three_speech_title = str(session['speaker_three_speech_title'])
        self.speaker_four = str(session['speaker_four'])
        self.speaker_four_speech_project = str(session['speaker_four_speech_project'])
        self.speaker_four_speech_title = str(session['speaker_four_speech_title'])
        self.ie_one = str(session['ie_one'])
        self.ie_two = str(session['ie_two'])
        self.ie_three = str(session['ie_three'])
        self.ie_four = str(session['ie_four'])
        self.sharing_master = str(session['sharing_master'])
        self.sharing_topic = str(session['sharing_topic'])


class MeetingDataModel:
    def __init__(self):
        self.club_name = 'AmazingFriday'
        self.meeting_datetime = '1800-01-01 17:00:00'
        self.monthly_theme = 'Reserve'
        self.saa = 'Reserve'
        self.tme = 'Reserve'
        self.ge = 'Reserve'
        self.ah_counter = 'Reserve'
        self.grammarian = 'Reserve'
        self.timer = 'Reserve'
        self.ttm = 'Reserve'
        self.table_topics_theme = 'Reserve'
        self.speaker_one = 'Reserve'
        self.speaker_one_speech_project = 'Reserve'
        self.speaker_one_speech_title = 'Reserve'
        self.speaker_two = 'Reserve'
        self.speaker_two_speech_project = 'Reserve'
        self.speaker_two_speech_title = 'Reserve'
        self.speaker_three = 'Reserve'
        self.speaker_three_speech_project = 'Reserve'
        self.speaker_three_speech_title = 'Reserve'
        self.speaker_four = 'Reserve'
        self.speaker_four_speech_project = 'Reserve'
        self.speaker_four_speech_title = 'Reserve'
        self.ie_one = 'Reserve'
        self.ie_two = 'Reserve'
        self.ie_three = 'Reserve'
        self.ie_four = 'Reserve'
        self.sharing_master = 'Reserve'
        self.sharing_topic = 'Reserve'

    def set(self, form):
        self.club_name = str(form['club_name']) if 'club_name' in form else self.club_name
        self.meeting_datetime = str(form['meeting_datetime']) if 'meeting_datetime' in form else self.meeting_datetime
        self.monthly_theme = str(form['monthly_theme']) if 'monthly_theme' in form else self.monthly_theme
        self.saa = str(form['saa']) if 'saa' in form else self.saa
        self.tme = str(form['tme']) if 'tme' in form else self.tme
        self.ge = str(form['ge']) if 'ge' in form else self.ge
        self.ah_counter = str(form['ah_counter']) if 'ah_counter' in form else self.ah_counter
        self.grammarian = str(form['grammarian']) if 'grammarian' in form else self.grammarian
        self.timer = str(form['timer']) if 'timer' in form else self.timer
        self.ttm = str(form['ttm']) if 'ttm' in form else self.ttm
        self.table_topics_theme = str(form['table_topics_theme']) if 'table_topics_theme' in form else self.table_topics_theme
        self.speaker_one = str(form['speaker_one']) if 'speaker_one' in form else self.speaker_one
        self.speaker_one_speech_project = str(form['speaker_one_speech_project']) if 'speaker_one_speech_project' in form else self.speaker_one_speech_project
        self.speaker_one_speech_title = str(form['speaker_one_speech_title']) if 'speaker_one_speech_title' in form else self.speaker_one_speech_title
        self.speaker_two = str(form['speaker_two']) if 'speaker_two' in form else self.speaker_two
        self.speaker_two_speech_project = str(form['speaker_two_speech_project']) if 'speaker_two_speech_project' in form else self.speaker_two_speech_project
        self.speaker_two_speech_title = str(form['speaker_two_speech_title']) if 'speaker_two_speech_title' in form else self.speaker_two_speech_title
        self.speaker_three = str(form['speaker_three']) if 'speaker_three' in form else self.speaker_three
        self.speaker_three_speech_project = str(form['speaker_three_speech_project']) if 'speaker_three_speech_project' in form else self.speaker_three_speech_project
        self.speaker_three_speech_title = str(form['speaker_three_speech_title']) if 'speaker_three_speech_title' in form else self.speaker_three_speech_title
        self.speaker_four = str(form['speaker_four']) if 'speaker_four' in form else self.speaker_four
        self.speaker_four_speech_project = str(form['speaker_four_speech_project']) if 'speaker_four_speech_project' in form else self.speaker_four_speech_project
        self.speaker_four_speech_title = str(form['speaker_four_speech_title']) if 'speaker_four_speech_title' in form else self.speaker_four_speech_title
        self.ie_one = str(form['ie_one']) if 'ie_one' in form else self.ie_one
        self.ie_two = str(form['ie_two']) if 'ie_two' in form else self.ie_two
        self.ie_three = str(form['ie_three']) if 'ie_three' in form else self.ie_three
        self.ie_four = str(form['ie_four']) if 'ie_four' in form else self.ie_four
        self.sharing_master = str(form['sharing_master']) if 'sharing_master' in form else self.sharing_master
        self.sharing_topic = str(form['sharing_topic']) if 'sharing_topic' in form else self.sharing_topic

    def update(self, key, value):
        if key and value:
            update_format = '{0}.{1} = {2}'.format(self, key, value)
            eval(update_format)
        else:
            pass
