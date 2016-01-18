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
        channel: number based on the numbering system specified (BCM or BOARD)
    setup(chan_list, GPIO.OUT)
        Set up more than one channel per call
    '''
    pass

@print_data
def output(*args, **kwargs):
    '''
    output(channel, value)
        set the output of a GPIO pin.
        channel: number based on the numbering system specified (BCM or BOARD).
        value: boolean
    '''
    pass

@print_data
def input(*args, **kwargs):
    '''
    input(channel)
        read the GPIO pin value.
        channel: number based on the numbering system specified (BCM or BOARD).
        returns boolean (true for HIGH value, false for LOW value).
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
    wait_for_edge(channel, edge)
        block program execution until an edge is detected
        edge = name of a transition from HIGH to LOW (falling) or LOW to HIGH (rising)
        edge -> GPIO.RISING or GPIO.FALLING or GPIO.BOTH
    wait_for_edge(channel, edge, timeout= # )
        block program execution for a certain lenght of time (timeout in miliseconds)
    '''
    pass

@print_data
def event_detected(*args, **kwargs):
    '''
    event_detected(channel)
        Reads events detected
        Pins must first be configured using add_event_detect
        returns boolean
    '''
    pass

@print_data
def add_event_detect(*args, **kwargs):
    '''
    add_event_detect(channel, edge, callbak(OPTIONAL), bouncetime(OPTIOPNAL))
        add event detection for a pin
        edge -> GPIO.RISING or GPIO.FALLING or GPIO.BOTH
    '''
    pass

@print_data
def add_event_callback(*args, **kwargs):
    '''
    add_event_callback(channel, callback, bouncetime(OPTIONAL))
        Adds an event callback function.
        callback: callback function to call on the event
        bouncetime: minimun time between two callbacks (in milliseconds)
    '''
    pass

@print_data
def remove_event_detect(*args, **kwargs):
    '''
    remove_event_detect(channel)
        remove events detection for a pin
    '''
    pass
