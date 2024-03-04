import logging 


logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='a.log',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )

logging.critical('file no exist error')