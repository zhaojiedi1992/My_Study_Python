_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}',
    # 'y': '{d.year}',
    # 'm': '{d.month}',
    # 'd': '{d.day}',
    }

class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
    
dt = MyDate(2022, 1, 1)
print(format(dt, 'mdy'))
print(format(dt, 'dmy'))
print(format(dt, 'ymd'))
# print(format(dt, 'y m d'))
# print('The date is {:ymd}'.format(dt))
print(format(dt, ''))