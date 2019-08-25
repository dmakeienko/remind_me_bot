from apscheduler.schedulers.background import BackgroundScheduler 
# from actions.remind import remind
from db.database import check_remind

scheduler = BackgroundScheduler()
print('scheduler started')
scheduler.add_job(check_remind, 'interval', minutes=1)
scheduler.start()
