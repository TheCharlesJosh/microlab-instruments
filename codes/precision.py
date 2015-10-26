#!/usr/bin/env python

# import microlab_instruments as mi
import sys

# TODO: Make this console-friendly
# TODO: Brush up your variable naming skills. Atienza shakes his head in disapproval

outputVolts = 5 if len(sys.argv) < 2 else sys.argv[1]				# volts, (failsafe at 5V)
limitCurr = 1E-3 if len(sys.argv) <	3 else sys.argv[2]			# amps, (failsafe at 1 mA)

# print len(sys.argv)
# print outputVolts
# print limitCurr

giratina = mi.Giratina()

def setVolt():
	print 'Voltage level at: {:>10} volts'.format(outputVolts)
	print 'Current limit at: {:>10} amperes'.format(limitCurr)

	giratina.write(':format:data real,64')
	giratina.write(':source1:function:mode voltage')
	giratina.write(':source1:function:shape dc')
	giratina.write(':source1:voltage: ' + outputVolts)
	giratina.write(':sense1:current:protection: ' + limitCurr)
	giratina.write(':output:state on')
	giratina.write(':initiate (@1)')

def fetchCurr():
	giratina.write(':read:scalar:current? (@1)')
	print 'Current current: {:>10} amperes'.format(giratina.read_ieee754())
