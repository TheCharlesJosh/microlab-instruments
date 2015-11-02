#!/usr/bin/env python

from precision import initVolt, setVolt
from oscui import autoScale, stats, plotData

initVolt()
setVolt(5, 0.2)
autoScale()
plotData('plot')
stats(100, 'vpp', True)
#stats(100, 'freq', True)


