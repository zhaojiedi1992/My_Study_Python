#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取当前日期
import datetime 
now = datetime.datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime.datetime(2024, 1, 2, 12, 20)
print(dt)


# datetime转换为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

dt = datetime.datetime(2024, 1, 2, 12, 20)
print(dt.timestamp())

# timestamp转换为datetime
dt = datetime.datetime.fromtimestamp(dt.timestamp())
print(dt)
print(datetime.utcfromtimestamp(dt)) # UTC时间

# str 2 datetime 

import datetime 
now =datetime.datetime.strptime("2024-01-01 18:00:00",'%Y-%m-%d %H:%M:%S')
print(now)

# datetime 2 str 

now_str =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now_str)

# 日期加减

now = datetime.datetime.now()
now + datetime.timedelta(hours=10,days=-1)

# 本地时间转化为utc时间

tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转化

utc_now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
bj_dt = utc_now.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
print(utc_now)
print(bj_dt)





