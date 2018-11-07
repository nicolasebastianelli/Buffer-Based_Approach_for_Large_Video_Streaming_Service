#!/usr/bin/env python
# -*- Mode: Python -*-
# -*- encoding: utf-8 -*-
# Nicola Sebastianelli <nicola.sebastianelli.95@gmail.com>
# Piergiorgio Ladisa <piergiorgio.ladisa@hotmail.it>

# This file may be distributed and/or modified under the terms of
# the GNU General Public License version 2 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE" in the source distribution for more information.
import os, sys
from utils_py.util import debug, format_bytes
from BaseController import BaseController

DEBUG = 1

# This controller is an implementation of the BBA0 Controller
# described in Chapter 4 of the paper:
# Zhi Li, et al, "A Buffer-Based Approach to Rate Adaptation: Evidence from a Large Video Streaming Service", Te-Yuan Huang, Ramesh Johari, Nick McKeown, Matthew Trunnell, Mark Watson Stanford University, Netflix

class BBA0Controller(BaseController):
    
def __init__(self):
    super(BBA0Controller, self).__init__()
    self.conf = {
        "r": 90,
        "cu": 126
    }

def __repr__(self):
    return '<BBA0Controller-%d>' %id(self)

def calcControlAction(self):
    self.setIdleDuration(0.0)
    
    # Retrive current iteration variables
    R_max= self.feedback['max_rate']
    R_min=self.feedback['min_rate']
    R_curr=self.feedback['cur_rate']
    Rates=self.feedback['rates']
    B_now = self.feedback['queued_time']
    
    # Compute upperbound
    if R_curr == R_max:
        R_plus = R_max
    else:
        R_plus = min(R_curr)

    # Compute lowerbound
    if R_curr == R_min:
        R_minus = R_min
    else:
        R_minus = max(R_curr)

    #Compute new rate based in current buffer region
    
    #Buffer in reservoir area
    if B_now <= self.conf["r"]:
        Rate_next= R_min

    #Buffer in upper reservoir area
    elif B_now >= self.conf["r"] + self.conf["cu"]:
        Rate_next = R_max

    #Buffer in cushion area
    elif f(Buf_now) >= R_plus:
        Rate_next= max(f(Buf_now))
    elif f(Buf_now) <= R_minus:
        Rate_next= min(f(Buf_now))

    else
        Rate_next=R_curr


    return Rate_next

def f(Buf_now):


def max(constraint):
    result=Rates[0]
    for each i in Rates[]:
        if Rates[i]> constraint & result> Rates[i]:
            result=Rates[i]
    return result

def min(constraint):
    result=Rates[0]
    for each i in Rates[]:
        if Rates[i]< constraint & result< Rates[i]:
            result=Rates[i]
    return result
                