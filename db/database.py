import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from dotenv import load_dotenv
import json
import datetime 
from dateutil.parser import parse
import logging
from db.Remind import Remind, Base
from utils.constants import DATETIME_FORMAT, EXPIRED_REMIND_TIME

load_dotenv()

logger = logging.getLogger('database')


engine = create_engine(os.environ['DB_URL'], pool_size=20, max_overflow=100)
Session = sessionmaker(bind=engine)


class RemindEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Remind):
            return obj.__dict__


# Generate database schema
Base.metadata.create_all(engine)

# Create new remind in DB
def create_remind(chat_id, time, text, expired=False, done=False):
    logger.info("Creating remind...")
    # Create a new session
    session = Session()
    parsed_time = parse(time)
    remind = Remind(chat_id, parsed_time, text, expired, done)
    session.add(remind)
    # Commit and close session
    session.commit()
    session.close()


def update_remind(chat_id, id, time, text):
    logger.info("Updating remind...")
    session = Session()
    session.query(Remind).filter_by(chat_id=chat_id).filter_by(id=id).one().update({"remind_time": parse(time), "remind_text": text})
    
    # Commit and close session
    session.commit()
    session.close()


def expire_remind(delete_id):
    session = Session()
    for i in delete_id:
        session.query(Remind).filter_by(id=i.id).update({"expired": True}, synchronize_session=False)

    # Commit and close session
    session.commit()
    session.close()


def get_reminds(user_chat_id):
    logger.info("Getting reminds...")
    session = Session()
    # Select all reminds with done == False, user is defined by chat_id
    reminds_list = session.query(Remind).filter_by(chat_id=user_chat_id).order_by(Remind.id).filter_by(done=False).all()
    json_data = json.loads(json.dumps(reminds_list, cls=RemindEncoder, indent=4))
    
    # Close session
    session.close()
    return json_data


def check_remind(*time):
    logger.info("Checking reminds...")
    session = Session()
    current_time=datetime.datetime.now().strftime(DATETIME_FORMAT)

    if not time:
        remind_time = current_time
        remind = session.query(Remind).filter_by(remind_time=remind_time).filter_by(expired=False).filter_by(done=False).all()
    elif time:
        if time[0] <= 3:
            remind_time = (datetime.datetime.strptime(current_time, DATETIME_FORMAT) - datetime.timedelta(minutes=time[0])).strftime(DATETIME_FORMAT)
            remind = session.query(Remind).filter_by(remind_time=remind_time).filter_by(expired=False).filter_by(done=False).all()
            logger.info("Checking NONEXPIRED...")
        else:
            delta = (datetime.datetime.strptime(current_time, DATETIME_FORMAT) - datetime.timedelta(minutes=time[0])).strftime(DATETIME_FORMAT)
            logger.info('delta time: ' + delta)
            remind = session.query(Remind).filter_by(expired=False).filter_by(done=False).filter(Remind.remind_time <= delta).all()
            remind_j = json.loads(json.dumps(remind, cls=RemindEncoder, indent=4))
            expire_remind(remind)
            logger.info('expiring remind')
            return 'expired', remind_j

    remind_j = json.loads(json.dumps(remind, cls=RemindEncoder, indent=4))
    if remind_j: 
        return remind_j
    # Close session
    session.close()


def close_remind(user_chat_id, id):
    logger.info("Closing reminds...")    
    session = Session()
    current_time=datetime.datetime.now().strftime(DATETIME_FORMAT)
    if not id:
        # TODO 
        # check if last remind exists
        remind = session.query(Remind).filter_by(chat_id=user_chat_id).filter_by(done=False).filter(Remind.remind_time <= current_time).order_by(desc(Remind.remind_time)).first()
        if remind is not None:
            session.query(Remind).filter_by(chat_id=user_chat_id).filter_by(id=remind.id).update({"done": True}, synchronize_session=False)
    else:
        for i in id:
            session.query(Remind).filter_by(chat_id=user_chat_id).filter_by(id=i).update({"done": True}, synchronize_session=False)
    # Commit and close session
    session.commit()
    session.close()


def delete_remind(delete_id, chat_id):
    logger.info("Deleting reminds...")
    session = Session()
    for i in delete_id:
        session.query(Remind).filter_by(id=i).filter_by(chat_id=chat_id).one().delete(synchronize_session=False)

    # Commit and close session
    session.commit()
    session.close()

