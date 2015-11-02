#!/usr/bin/env python

import microlab_instruments as mi
import numpy as np
import math
import time

# TODO: Make this console-friendly
# TODO: Brush up your variable naming skills. Atienza shakes his head in disapproval

giratina = mi.Giratina()

def siPrefix(number):
	_prefix = 'yzafpnum kMGTPEZY'
	return str(number / (10.00 ** ((int(math.log(abs(number), 10)) / 3) * 3))) + _prefix[((int(math.log(abs(number), 10)) / 3)) + 8]

def initVolt():
	giratina.write(':source1:function:mode voltage')
	giratina.write(':source1:function:shape dc')
	while giratina.ask_ascii('*OPC?'):
		break
	print 'Ready!'


def setVolt(outputVolts, limitCurr):
	print 'Voltage level at: {:>10} volts'.format(outputVolts)
	print 'Current limit at: {:>10} amperes'.format(limitCurr)

	giratina.write(':source1:voltage ' + str(outputVolts))
	giratina.write(':sense1:current:protection ' + str(limitCurr))
	giratina.write(':format:data real,64')
	giratina.write(':output:state on')

def fetchCurr():
	giratina.write(':init:acq (@1)')
	giratina.write(':fetch:scalar:current? (@1)')
	catchCurr = giratina.read_ieee754()[0]
	print 'Current current:  {:>10} (A)'.format(siPrefix(catchCurr))

# def oscilloscope():
#	x = np.arange(0, 1.0/60.0, 0.0002)

#	y = np.sin(2 * np.pi * x * 60)
#	z = ['%.4f' % elem for elem in y.tolist()]
#	j = [float(k) for k in z]
#	initVolt()
#	while True:
#		for num in j:
#			setVolt(num, 0.01)
#			time.sleep(0.0002)

#initVolt()
#setVolt(5, 0.2)
#fetchCurr()
