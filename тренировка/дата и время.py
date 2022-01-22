# datetime.date
import datetime
print(datetime.date(2020, 2, 12))

d = datetime.date(2020, 1, 13)
print(d.year)
print(d.day)
print(d.month)

print(datetime.date.today()) #Сегодняшняя дата

a = datetime.datetime(2017, 3, 5)
print(a) # datetime.datetime(2017, 3, 5, 0, 0)

b = datetime.datetime(2017, 3, 5, 12, 30, 10)
print(b) # datetime.datetime(2017, 3, 5, 12, 30, 10)

d = datetime.datetime(2017, 3, 5, 12, 30, 10)
print(d.year) # 2017
print(d.second) # 10
print(d.hour) # 12

t = datetime.datetime.today()
print(t)

n = datetime.datetime.now()
print(n)

a1 = datetime.datetime.today().strftime("%Y%m%d")
print(a1)

today = datetime.datetime.today()
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%y-%m-%d-%H-%M-%S")) # Y заменен на y для сокращения до 2-х чисел

now = datetime.datetime.now()
then = datetime.datetime(2020,6,18)

delta = now - then

print(delta.days)
print(delta.seconds)

seconds = delta.total_seconds()
hours = seconds // 3600
print(hours)

minutes = (seconds % 3600) // 60
print(minutes)

import time
print(time.gmtime(0))

print(time.ctime())

print(time.ctime(1384112639))

for x in range(1):
    time.sleep(2)
    print("Slept for 2 seconds")

a24 = time.strftime("%Y-%m-%d-%H.%M-%S", time.localtime())
print(a24)

x1 = time.time()
print(x1)

x2 = time.ctime(time.time())
print(x2)