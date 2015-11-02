import microlab_instruments as mi
import matplotlib.pyplot as plotlab
import numpy as np
import math

deoxys = mi.Deoxys()

def siPrefix(number):
	_prefix = 'yzafpnum kMGTPEZY'
	if number != 0:
		return (str(number / (10.00 ** ((int(math.ceil(math.log(abs(number), 10))) / 3) * 3))) + _prefix[((int(math.ceil(math.log(abs(number), 10))) / 3)) + 8])

def plotData(ops='plot', minIndex=None, maxIndex=None):
	timePerDiv = float(deoxys.ask_ascii(':timebase:range?'))
	data = ''	

	# Retrieving the data from the oscilloscope
	deoxys.write(':acquire:type:normal')
	deoxys.write(':digitize')
	deoxys.write(':waveform:points 1000')
	deoxys.write(':waveform:byteorder msbfirst')
	deoxys.write(':waveform:format ascii')
	deoxys.write(':waveform:data?')

	# Grab all points from memory
	while True:
		temp = deoxys.read()
		data += temp
		if '\n' == temp[-1:]:
			break

	# Parse strings into floating points
	voltagePoints = np.array([float(strPoint) for strPoint in data[10:].split(',')])
	timePoints = np.linspace(0, timePerDiv * 10, len(voltagePoints))
	deoxys.write(':autoscale')
	plotlab.plot(timePoints, voltagePoints)
	if ops == 'plot':
		plotlab.show()
	elif ops == 'prettifyraw':
		for (secs, volts) in zip(timePoints[minIndex:maxIndex], voltagePoints[minIndex:maxIndex]):
			print '{:10.10f} {:10.10f}'.format(secs, volts)
	elif ops == 'prettifyengg':
		for (secs, volts) in zip(timePoints[minIndex:maxIndex], voltagePoints[minIndex:maxIndex]):
			print '{}secs\t{}V'.format(siPrefix(secs), siPrefix(volts))

	return [(timePoints[i], voltagePoints[i]) for i in range(len(voltagePoints))] if ops == 'points' else None

def autoScale():
	deoxys.write(':autoscale')

def getFreq(prettify=False):
	#TODO The universes* have no edge.
	deoxys.write(':measure:frequency?')
	return siPrefix(float(deoxys.read())) if prettify else float(deoxys.read())

def getVpp(prettify=False):
	deoxys.write(':measure:vpp?')
	return siPrefix(float(deoxys.read())) if prettify else float(deoxys.read())

def getVabs(prettify=False):
	deoxys.write(':measure:vaverage?')
	return siPrefix(float(deoxys.read())) if prettify else float(deoxys.read())

def stDev(samples, ops='vpp', prettify=False):
	a = []
	for x in range(0, samples):
		if ops == 'vpp':
			a.append(getVpp())
		if ops == 'vabs':
			a.append(getVabs())
		elif ops == 'freq':
			a.append(getFreq())
	return siPrefix(np.std(a)) if prettify else np.std(a)

def mean(samples, ops='vpp', prettify=False):
	a = []
	for x in range(0, samples):
		if ops == 'vpp':
			a.append(getVpp())
		elif ops == 'vabs':
			a.append(getVabs())		
		elif ops == 'freq':
			a.append(getFreq())
	return siPrefix(np.mean(a)) if prettify else np.mean(a)

def stats(samples, ops='vpp', prettify=False):
	a = []
	for x in range(0, samples):
		if ops == 'vpp':
			a.append(getVpp())
		if ops == 'vabs':
			a.append(getVabs())
		elif ops == 'freq':
			a.append(getFreq())
	print '{:>30}: {}'.format('Standard Dev ({})'.format('V' if ops == 'vpp' or ops == 'vabs' else 'Hz'), siPrefix(np.std(a)))
	print '{:>30}: {}'.format('Mean ({})'.format('V' if ops == 'vpp' or ops == 'vabs' else 'Hz'), siPrefix(np.mean(a)))

#autoScale()
#plotData('plot')
stats(100, 'vabs', True)
#stats(100, 'freq', True)
#print '{:>30}: {}'.format('Standard Dev (V)', stDev(250, 'volts', True))
#print '{:>30}: {}'.format('Standard Dev (Hz)', stDev(250, 'freq', True))
#print '{:>30}: {}'.format('Mean (V)', mean(250, 'volts', True))
#print '{:>30}: {}'.format('Mean (Hz)', mean(250, 'freq', True))
#print '{:>30}: {}'.format('Frequency (Hz)', getFreq(True))
#print '{:>30}: {}'.format('Peak-to-Peak Voltage (V)', getVpp(True))
