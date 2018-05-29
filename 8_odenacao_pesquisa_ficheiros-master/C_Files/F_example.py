"""
Files -example
"""

import time

log_file = open("_test_files/log.txt", "a")

message = "Started"

log_file.write("\n{} - {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), message))

log_file.close()
