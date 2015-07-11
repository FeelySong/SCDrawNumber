
import datetime
import random
import time
zeroyear=datetime.datetime.today().year
zeromonth=datetime.datetime.today().month
zeroday=datetime.datetime.today().day
zerotime = datetime.datetime(year=zeroyear, month=zeromonth, day=zeroday, hour=0, minute=0, second=0)
zerotime1 = datetime.datetime.now()
datetoday= time.strftime("%y%m%d")
dateissue = str(int((zerotime1 - zerotime).seconds / 60))
draw_date=datetoday+dateissue
draw_code = str(random.randint(10000,99999))
print draw_date,draw_code,datetime.datetime.now()