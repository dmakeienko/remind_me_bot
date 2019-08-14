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
        self.remind_day = remind_day
        self.remind_time = remind_time
        self.remind_text = remind_text
        self.expired = expired



class RemindEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Remind):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


# Generate database schema
Base.metadata.create_all(engine)

# Create new remind in DB
def create_remind(day, time, text, expired):
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


def delete_remind():
    session = Session()

    
    # Commit and close session
    session.commit()
    session.close()


def get_reminds():
    session = Session()
    res = session.query(Remind).all()
    
    # Close session
    session.close()
    return json.dumps(res, cls=RemindEncoder)