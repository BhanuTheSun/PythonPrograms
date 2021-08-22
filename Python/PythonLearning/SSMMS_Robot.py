import schedule
import time
import os

def job():
    os.system('"C:\SandBooking\SSMMS_V1.3\SSMMS_V1.3\SSMMS V1.3.exe"')
schedule.every().day.at("11:59:59").do(job)


while True:
    schedule.run_pending()
    time.sleep(0.1)
