# (I don't know what to call this document)
# Created by Charles Alba and Kyle Gomez.

import microlab_instruments as mi
import matplotlib.pyplot as plotlab
import numpy as np
import math
import time

deoxys = mi.Deoxys()
giratina = mi.Giratina()

values = {
	#'all': 'on',
	'current': 'current',
	'min': 'minimum',
	'max': 'maximum',
	'mean': 'mean',
	'std dev': 'stdd',
	'count': 'count'
}

measures = {
	'vpp': 'Vpp (V)',
	'freq': 'Frequency (Hz)',
	'vdc': 'DC Voltage (V)'
}

def siPrefix(number):
	_prefix = 'yzafpnum kMGTPEZY'
	if number != 0:
		return (str(number / (10.00 ** ((int(math.ceil(math.log(abs(number), 10))) / 3) * 3))) + _prefix[((int(math.ceil(math.log(abs(number), 10))) / 3)) + 8])

# Functions to consider for the oscilloscope functions:
# getMeas()		Args: from mode (vpp, freq, vdc), required value (stddev...), Raw (Optional)
# autoScale()	Args: None
# quickMeas() 	Args: Raw (Optional)

def autoScale():
	deoxys.write(':autoscale')

def quickMeas():
	deoxys.write(':autoscale')
	deoxys.write(':marker:mode off')
	deoxys.write(':marker:mode measurement')

#getMeas needs to have autoScale and quickMeas run before it for it to work.
def getMeas(mode, data, format='SI'):
	if mode=='vpp':
		deoxys.write(':measure:vaverage?')
		print '{:>15}: {}'.format(measures[mode], siPrefix(float(deoxys.read())) if format=='SI' else float(deoxys.read()))
		return siPrefix(float(deoxys.read())) if format=='SI' else float(deoxys.read())

	deoxys.write(':measure:statistics {}'.format(values[data]))
	deoxys.write(':measure:results?')
	result = deoxys.read()[:-1]

	print '{:>15}: {}'.format(measures[mode], siPrefix(float(result.split(',', 1)[1 if mode == 'vpp' else 0])) if format=='SI' else float(result.split(',', 1)[1 if mode == 'vpp' else 0]))
	return siPrefix(float(result.split(',', 1)[1 if mode == 'vpp' else 0])) if format=='SI' else float(result.split(',', 1)[1 if mode == 'vpp' else 0])
