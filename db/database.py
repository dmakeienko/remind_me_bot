import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import json

load_dotenv()

engine = create_engine(os.environ['DB_URL'])
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Remind(Base):
# TODO add chat id
    __tablename__ = 'reminds'
    id = Column(Integer, primary_key=True)
    remind_day = Column(String(10))
    remind_time = Column(String(8))
    remind_text = Column(String(100))
    expired = Column(Boolean, default=False)

    def __init__(self, remind_day, remind_time, remind_text, expired):
        # self.id = id
        self.remind_day = remind_day
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
def create_remind(day, time, text, expired=False):
    # Create a new session
    session = Session()

    remind = Remind(day, time, text, expired)
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
    # delete_id_to_int = delete_id[0]
    session.query(Remind).filter_by(id=delete_id[0]).update({"expired": True}, synchronize_session=False)

    # Commit and close session
    session.commit()
    session.close()


def get_reminds():
    session = Session()
    # Select all reminds with expired == False
    reminds_list = session.query(Remind).order_by(Remind.id).filter_by(expired=False).all()
    json_data = json.loads(json.dumps(reminds_list, cls=RemindEncoder, indent=4))
    
    # Close session
    session.close()
    return json_data