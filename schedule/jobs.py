import schedule
import time
import sys
# sys.path.append('../db')
from db.database import check_remind

schedule.every(5).minutes.do(check_remind)


# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
   
# Checks whether a scheduled task  
# is pending to run or not 
  schedule.run_pending() 
  time.sleep(1) 

