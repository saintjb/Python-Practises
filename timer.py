import time
import os


sec = 0
min = 0
while True:
    sec += 1
    print(str(min) + ' Minutes ' + str(sec) + ' Seconds')
    time.sleep(1)
    if sec == 60:
        sec = 0
        min += 1
    os.system('clear')
