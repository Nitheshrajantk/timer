# Script Name        :  timer.py
# Author             :  Nithesh
# Created            :  August 03 2020
# Last modified      :
# Version            :  1.2.1
# Description        :  Timer that writes remaining time in a file in same directory.

from datetime import datetime, timedelta
from time import sleep
import os, sys
from settings import *

## String processing functions
def spit(minutes, seconds):
    if minutes == 0:
        output = formats['singleSeconds'].format(seconds)
    elif minutes > 0 and seconds < 10:
        output = formats['paddedSeconds'].format(minutes, seconds)
    else:
        output = formats['fullSeconds'].format(minutes, seconds)
    file.write(output)
    return output

def cmdPrint(i, printClearEnable):
    if printClearEnable == True:
        os.system(clear)
    print('Script running{} [{}] (Please only shut me down using ctrl + c)'.format(dots[i], output))

def kill():
    file = open("timer.txt", "w")
    file.write(finishMessage)
    file.close()

# Initial countdown time calculation
if topOfHour == True:
    now = datetime.now
    cdTime = datetime(year=now().year,
                         month=now().month,
                         day=now().day,
                         hour=now().hour + 1) - now()
    cdTime = cdTime.seconds
else:
    cdTime = int(float(input('How many minutes? (Default: {}) '.format(defaultCountdownTime)) or 10) * 60)

## Actual process
i = 0
try:
    while True:
        # Divide countdown time into minutes and seconds
        minutes = int(cdTime / 60)
        seconds = cdTime % 60

        # Formats, writes and outputs strings
        file = open("timer.txt", "w")
        if minutes <= 0 and seconds < reductionAmount: # Normal exit condition
            file.write('0')
            file.close()
            sleep(tick)
            break
        output = spit(minutes, seconds)
        file.close()

        # Print stuff to command line
        if printClearEnable == True:
            cmdPrint(i, True)
        else:
            cmdPrint(i, False)
        i = (i + 1) % len(dots)

        cdTime -= reductionAmount
        sleep(tick)
#except KeyboardInterrupt:
except:
    kill()
    print('Timer cancelled. Output set to "finished" value. (See settings.py to change it.)')
    sleep(tick)
    sys.exit()

kill()
print('Countdown finished. Output set to "finished" value. (See settings.py to change it.)')
sleep(5)
