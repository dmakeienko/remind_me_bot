import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import json
import datetime 
from dateutil.parser import parse


load_dotenv()

engine = create_engine(os.environ['DB_URL'])
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Remind(Base):
    __tablename__ = 'reminds'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    remind_time = Column(String(20))
    remind_text = Column(String(100))
    expired = Column(Boolean, default=False)

    def __init__(self, chat_id, remind_time, remind_text, expired):
        self.chat_id = chat_id
        self.remind_time = remind_time
        self.remind_text = remind_text
        self.expired = expired



class RemindEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Remind):
            return obj.__dict__


# Generate database schema
Base.metadata.create_all(engine)

# Create new remind in DB
def create_remind(chat_id, time, text, expired=False):
    # Create a new session
    session = Session()
    parsed_time = parse(time)
    remind = Remind(chat_id, parsed_time, text, expired)
    session.add(remind)
    # Commit and close session
    session.commit()
    session.close()


def update_remind():
    session = Session()

    
    # Commit and close session
    session.commit()
    session.close()


def expire_remind(delete_id):
    session = Session()
    session.query(Remind).filter_by(id=delete_id[0]).update({"expired": True}, synchronize_session=False)

    # Commit and close session
    session.commit()
    session.close()


def get_reminds(user_chat_id):
    session = Session()
    # Select all reminds with expired == False, user is defined by chat_id
    reminds_list = session.query(Remind).order_by(Remind.id).filter_by(expired=False).filter_by(chat_id=user_chat_id).all()
    json_data = json.loads(json.dumps(reminds_list, cls=RemindEncoder, indent=4))
    
    # Close session
    session.close()
    return json_data


def check_remind():
    session = Session()
    current_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:00')
    # current_time = '2019-08-20 23:15:00'
    remind = session.query(Remind).filter_by(remind_time=current_time).filter_by(expired=False).all()

    remind_j = json.loads(json.dumps(remind, cls=RemindEncoder, indent=4))
    if remind_j: 
        return(remind_j)

    # Close session
    session.close()


check_remind()