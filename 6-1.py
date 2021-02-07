# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:38:15 2019

@author: aaaaa
"""

import schedule
import time

def job():
    print("I'm working...")

schedule.every(20).seconds.do(job) #每10秒執行一次
#schedule.every().hour.do(job) #每小時執行一次
#schedule.every().day.at("9:30").do(job) #每天9點30執行一次
#schedule.every().monday.do(job) #每週一執行一次
#schedule.every().wednesday.at("14:45").do(job) #每週三14點45執行一次

# 無窮迴圈
while True: 
    schedule.run_pending()
    time.sleep(1)
