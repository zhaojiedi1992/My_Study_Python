import configparser
cfg = configparser.ConfigParser()
cfg.read('./demo.ini')
print(cfg.get('server','nworkers'))