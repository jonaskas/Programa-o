"""
logging
"""

import os
import logging

filePath = os.path.join("_temp", "log.log")

print("Logging to", filePath) 

logging.basicConfig( \
    level=logging.DEBUG, \
    format='%(asctime)s : %(levelname)s : %(message)s', \
    filename=filePath, \
    filemode='w') # a to append

logging.debug("Starting...")
for i in range(100, -1, -1):
    logging.info("iteration: {}".format(i))
    if i == 50:
        logging.warning("half the way")
    elif i == 25:
        logging.critical("A critical message at 25")
    elif i == 10:
        logging.error("An error message at 10")
logging.debug("Done...")
