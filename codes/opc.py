#!/usr/bin/env python

import microlab_instruments as mi
import time

genesect = mi.Genesect()
initTime = time.time()
while genesect.ask_ascii('*OPC?'):
	print time.time() - initTime
	break
	#deoxys.write(':autoscale')
