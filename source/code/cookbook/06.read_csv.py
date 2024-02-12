import csv
from collections import namedtuple

# 列表方式
with open('./stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print('headers:{}'.format(headers))

    for row in f_csv:
        print(row[0])


# 命名元组方式
with open('./stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print('headers:{}'.format(headers))
    Row = namedtuple('Row',headers)
    for r in f_csv:
         row = Row(*r)
         print(row.Symbol)

# 字典方式
with open('./stocks.csv') as f:
    f_csv = csv.DictReader(f)
    headers = next(f_csv)
    print('headers:{}'.format(headers))
  
    for row in f_csv:
         print(row['Symbol'])



