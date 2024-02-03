from datetime import datetime,timedelta
import calendar

def get_start_and_end_of_month(dt=None):
    if dt is None:
        dt = datetime.today()
    start_dt = dt.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    end_dt = start_dt + timedelta(days=31)
    for diff in (31,30,29,28):
        if start_dt.month != end_dt.month:
            break
        end_dt = start_dt + timedelta(days=diff)
    return start_dt,end_dt

def get_start_and_end_of_month_v2(dt=None):
    if dt is None:
        dt = datetime.today()
    start_dt = dt.replace(day=1,hour=0,minute=0,second=0,microsecond=0)
    _, days_in_month = calendar.monthrange(start_dt.year, start_dt.month)
    end_dt = start_dt + timedelta(days=days_in_month)
    return start_dt,end_dt

def range_dt(start_dt,end_dt,timedelta=timedelta(days=1)):
    while start_dt < end_dt:
        yield start_dt
        start_dt += timedelta
   

start_dt,end_dt = get_start_and_end_of_month()
print(start_dt,end_dt)

start_dt,end_dt = get_start_and_end_of_month_v2()
print(start_dt,end_dt)

for dt in range_dt(start_dt,end_dt,timedelta(hours=6)):
    print(dt)

 









    
