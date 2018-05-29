"""
Time
See: https://docs.python.org/3.6/library/time.html
"""

import time

def sleep_inc(value):
    for x in range(value):
        print("Sleeping for {} seconds".format(x))
        time.sleep(x)

print(time.strftime('%Y%m%d%H%M%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(time.ctime())

print(time.gmtime(0)) # Epoch

time1 = time.time() #ticks
print(time1, "ticks")
time1 = time.localtime(time1) #struct
print(time1)
print(time1[0])
time1 = time.asctime(time1)
print(time1)

sleep_inc(5)
