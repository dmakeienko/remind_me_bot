from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Remind(Base):
    __tablename__ = 'reminds'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    remind_time = Column(String(20))
    remind_text = Column(Text)
    expired = Column(Boolean, default=False)
    done = Column(Boolean, default=False)


    def __init__(self, chat_id, remind_time, remind_text, expired, done):
        self.chat_id = chat_id
        self.remind_time = remind_time
        self.remind_text = remind_text
        self.expired = expired
        self.done = done