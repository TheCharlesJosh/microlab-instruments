#!/usr/bin/env python

import microlab_instruments as mi

giratina = mi.Giratina()

print giratina.ask_ascii('*OPC?')
