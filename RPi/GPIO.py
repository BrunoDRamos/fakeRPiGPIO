#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Fake RPi.GPIO package
'''
#______________________________________________________________________
# imports

#______________________________________________________________________
# globals
BCM = 'BCM'
BOARD = 'BOARD'

OUT = 'OUT'
IN = 'IN'

LOW = 'LOW'
HIGH = 'HIGH'

RISING = 'RISING'

PUD_UP = 'PUD_UP'
PUD_DOWN = 'PUD_DOWN'

RPI_INFO = {'INFO': 'Fake GPIO, ¬¬', 'P1_REVISION': 'Fake GPIO, ¬¬'}

VERSION = '0.2.0a0'

#______________________________________________________________________
# VERBOSE
VERBOSE = True

#______________________________________________________________________
# functions wrapper/ base fucntion
def print_data(func):
    def verbose(*args, **kwargs):
        if VERBOSE:
            print(func.__name__, args, kwargs)
    return verbose

#______________________________________________________________________
# PWM class
class PWM(object):

    @print_data
    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.dc = 0

    @print_data
    def start(self, dc):
        pass

    @print_data
    def ChangeFrequency(self, freq):
        self.frequency = freq

    @print_data
    def ChangeDutyCycle(self, dc):
        self.dc = dc

    @print_data
    def stop(self):
        pass

#______________________________________________________________________
# functions

@print_data
def setmode(*args, **kwargs):
    '''
    setmode(GPIO.BCM or GPIO.BOARD)
        Sets the pin mode
        BCM refers to the channel numbers on the Boardcom SOC
        BOARD refers to pin numbers on the P1 header of the Raspberry Pi board
    '''
    pass

@print_data
def setup(*args, **kwargs):
    '''
    setup(channel, GPIO.IN or channel, GPIO.OUT)
        Setup channel as input or output
        channel = number based on the numbering system specified (BCM or BOARD)
    setup(chan_list, GPIO.OUT)
        Set up more than one channel per call
    '''
    pass

@print_data
def output(*args, **kwargs):
    '''
    output(channel, state)
        set the output state of a GPIO pin
        channel = number based on the numbering system specified (BCM or BOARD)
    '''
    pass

@print_data
def input(*args, **kwargs):
    '''
    input(channel)
        read the value of a GPIO pin
        channel = number based on the numbering system specified (BCM or BOARD)
    '''
    pass

@print_data
def cleanup(*args, **kwargs):
    '''
    cleanup()
        clean up used resources at the end of script
    cleanup(channel)
        clean up individual, a list or a tuple of channels
    '''
    pass

@print_data
def wait_for_edge(*args, **kwargs):
    '''
    wait_for_edge(channel, GPIO.RISING or GPIO.FALLING or GPIO.BOTH)
        block program execution until an edge is detected
        edge = name of a transition from HIGH to LOW (falling) or LOW to HIGH (rising)
    '''
    pass

@print_data
def event_detected(*args, **kwargs):
    pass

@print_data
def add_event_detect(*args, **kwargs):
    pass

@print_data
def add_event_callback(*args, **kwargs):
    pass

@print_data
def remove_event_detect(*args, **kwargs):
    pass
