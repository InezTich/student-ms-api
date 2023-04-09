import logging

logging.basicConfig(level=logging.DEBUG, filename='applogs.log')

logging.debug("Application logger is working")
logging.info("This is the info data")
logging.error({'status': 1,'message':'Can not login to application server, somthing went wrong!!!'})