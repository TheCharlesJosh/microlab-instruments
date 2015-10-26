#!/usr/bin/env python
import microlab_instruments as mi
from os import fsync
from random import randint
import numpy as np

#aardvark = mi.AardvarkInstrument()
#print aardvark

#darkrai = mi.Darkrai()
#print darkrai.ask_ascii('*IDN?'),
#deoxys = mi.Deoxys()
#print deoxys.ask_ascii('*IDN?'),
#genesect = mi.Genesect()
#print genesect.ask_ascii('*IDN?'),
#giratina = mi.Giratina()
#print giratina.ask_ascii('*IDN?'),
#heatran = mi.Heatran()
#print heatran.ask_ascii('*IDN?'),
#ho_oh = mi.Ho_oh()
#print ho_oh.ask_ascii('*IDN?'),
#kyurem = mi.Kyurem()
#print kyurem.ask_ascii('*IDN?'),
#yveltal = mi.Yveltal()
#print yveltal.ask_ascii('*IDN?'),

giratina = mi.Giratina()
#yveltal.write('*STB?')
#yveltal.write('*IDN?')
#q0 = yveltal.read()
#q1 = yveltal.read()
#print '{0:08b}'.format(int(q0))

def tutorial():
    """When querying the status registers, bit 0 is at the right.
    Big-endian.
    """
    giratina.write(':source:function:mode voltage')
    giratina.write(':source:sweep:direction up')
    giratina.write(':source:sweep:stair double')
    giratina.write(':source:sweep:spacing linear')
    giratina.write(':source:voltage:mode sweep')
    giratina.write(':source:voltage:start 0')
    giratina.write(':source:voltage:stop 5')
    giratina.write(':source:voltage:points 201')
    giratina.write(':sens:curr:prot 0.120')
    giratina.write(':trigger:source aint')
    giratina.write(':trigger:count 201')
    giratina.write(':format:data real,64')
    giratina.write(':outp on')
    giratina.write(':init (@1)')
    stb0 = giratina.ask_ascii('*STB?')
    print '{0:08b}'.format(int(stb0))
    giratina.ask_ascii('*OPC?')
    giratina.write(':output off')
    stb0 = giratina.ask_ascii('*STB?')
    print '{0:08b}'.format(int(stb0))
    esr0 = giratina.ask_ascii('*ESR?')
    print '{0:08b}'.format(int(esr0))
    giratina.write(':fetch:arr:volt? (@1)')
    volt = np.array(giratina.read_ieee754())
    giratina.write(':fetch:arr:curr? (@1)')
    curr = np.array(giratina.read_ieee754())
    res  = volt / curr
    for m, n, o in zip(volt, curr, res):
        a = '{0:>20.3e}'.format(m)
        b = '{0:>17.1f}mA'.format(n*1e3)
        c = '{0:>20.3e}'.format(o)
        print ''.join([a, b, c])


def screenshot():
    print giratina.write(':DISP:ENAB ON')
    print giratina.write(':format:data real,32')
    print giratina.write(':DISP:VIEW GRAPH')
    print giratina.write(':HCOP:SDUM:FORM JPG')
    print giratina.write('*OPC')
    #s = giratina.ask_ascii('*OPC?')
    giratina.write(':HCOP:SDUM:DATA?')
    giratina.write(':DISP:WIND:DATA?')
    d = giratina.read_binary()

    #print len(d)
    #print hex(ord('\n'))
    #print hex(ord(d[-1]))

    #for a in d[:10]:
        #for c in a:
            #print hex(ord(c)), c

    fd = open('dump.jpg', 'wb')
    fd.write(d)
    fd.close()

tutorial()
#screenshot()
