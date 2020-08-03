# Script Name        :  settings.py
# Author             :  Nithesh
# Created            :  August 03rd 2020
# Last modified      :
# Version            :  1.1
# Description        :  Settings file for timer.py.
from random import choice

''' TIMER SETTINGS: '''
    # Force timer to countdown to top of hour (True/False)
topOfHour = False

    # Default countdown time in minutes
defaultCountdownTime = 10

    # How many seconds are reduced at each tick
reductionAmount = 1

    # How long is one tick in seconds
tick = 1

    # What is displayed when the timer runs out. Replace, add or remove lines as needed.
    # Random choices from the list below.
finishMessage = choice([
    'WOO',
    'NOW',
    'READY',
    'GO',
    'PEANUTS',
    ])
    # Permanent choice. Overrides the list above. (Remove the # from the line below)
#finishMessage = ' '


''' STRING DICTIONARIES: '''
    # Customize time format to your liking
formats = {
        'singleSeconds': '{}',
        'fullSeconds': '{}:{}',
        'paddedSeconds': '{}:0{}',
        }

    # Add some dots or take away or whatever, mhm..
dots = [
        '.    ',
        '..   ',
        '...  ',
        '.... ',
        '.....',
        ]

''' DEVELOPER SETTINGS: '''
    # Is terminal cleared every tick (True/False)
printClearEnable = True
    # Terminal clearing command. Use 'cls' for windows, 'clear' for linux systems.
clear = 'cls'            
    # Query variables:
#reductionAmount = raw_input('Reduction per second? (Default: 1 s) ') or 1
#tick = 1 / (raw_input('Tickrate? (Default: 1 tick/sec) ') or 1)
#printClearEnable = raw_input('Clear command line at tick? (Default: True) ') or True
