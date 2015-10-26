#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base_classes as bc
from struct import pack, unpack

# FPGA Instruments
DEOXYS = {
    'nickname': 'deoxys',
    'name': 'Xilinx Virtex 5',
    'address': 0x55,
    }

# I2C Instruments
MELEOTTA = {
    'nickname': 'meleotta',
    'name': 'I2C Mux Thing',
    'address': 0x70,
    }
ARIA = {
    'nickname': 'aria',
    'name': 'Sensirion STS21 Temperature Sensor',
    'address': 0x4A,
    'mux_address': 0x04,
    }
PIROUETTE = {
    'nickname': 'pirouette',
    'name': 'Sensirion STS21 Temperature Sensor',
    'address': 0x4A,
    'mux_address': 0x05,
    }

# GPIB Instruments
RAYQUAZA = {
    'nickname': 'rayquaza',
    'name': 'Agilent 8753ES S-Parameter Network Analyzer',
    'get_byte_order': '',
    'byte_order_little': '',
    }
GROUDON = {
    'nickname': 'groudon',
    'name': 'Hewlett-Packard 6623A System DC Power Supply',
    'get_byte_order': '',
    'byte_order_little': '',
    }
KYOGRE = {
    'nickname': 'kyogre',
    'name': 'Hewlett-Packard 4156A Precision Semiconductor Parameter Analyzer',
    'get_byte_order': '',
    'byte_order_little': '',
    }

# TCPIP Instruments
KYUREM = {
    'nickname': 'kyurem',
    'name':  'Agilent N9020A MXA Signal Analyzer',
    'socket': ('192.168.1.5', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }
ZYGARDE = {
    'nickname': 'zygarde',
    'name': 'Agilent InfiniiVision MSO7104A Mixed Signal Oscilloscope',
    'socket': ('192.168.1.10', 5025),
    'get_byte_order': ':waveform:byteorder?',
    'byte_order_little': 'LSBF',
    }
DIALGA = {
    'nickname': 'dialga',
    'name': 'Agilent B2962A Power Source',
    'socket': ('192.168.1.9', 5025),
    'get_byte_order': ':format:border?',
    'byte_order_little': 'NORM',
    'get_data_format': ':format:data?',
    'data_format_single': 'REAL,32',
    'data_format_double': 'REAL,64',
    }
PALKIA = {
    'nickname': 'palkia',
    'name': 'Agilent B2962A Power Source',
    'socket': ('192.168.1.8', 5025),
    'get_byte_order': ':format:border?',
    'byte_order_little': 'NORM',
    'get_data_format': ':format:data?',
    'data_format_single': 'REAL,32',
    'data_format_double': 'REAL,64',
    }
REGIGIGAS = {
    'nickname': 'regigigas',
    'name': 'Agilent 16803A Logic Analyzer',
    'socket': ('192.168.1.11', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }
XERNEAS = {
    'nickname': 'xerneas',
    'name': 'Agilent N5182A MXG Vector Signal Generator',
    'socket': ('192.168.1.4', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }
YVELTAL = {
    'nickname': 'yveltal',
    'name': 'Agilent N5183A MXG Analog Signal Generator',
    'socket': ('192.168.1.3', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }
ZEKROM = {
    'nickname': 'zekrom',
    'name': 'Agilent E4443A PSA Series Spectrum Analyzer',
    'socket': ('192.168.1.2', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }
GIRATINA = {
    'nickname': 'giratina',
    'name': 'Agilent B2902A Precision Source/Measure Unit',
    'socket': ('192.168.1.7', 5025),
    'get_byte_order': ':format:border?',
    'byte_order_little': 'NORM',
    'get_data_format': ':format:data?',
    'data_format_single': 'REAL,32',
    'data_format_double': 'REAL,64',
    }
RESHIRAM = {
    'nickname': 'reshiram',
    'name': 'Agilent E5071C ENA Series Network Analyzer',
    'socket': ('192.168.1.6', 5025),
    'get_byte_order': '',
    'byte_order_little': '',
    }


class Deoxys(bc.FPGAInstrument):
    def __init__(self, aardvark):
        """Initialize the FPGA.

        :param Aardvark aardvark:
                An Aardvark object through which I2C commands are relayed.

        .. code-block:: python

            import microlab_instruments as mi

            aa = mi.Aardvark()
            deoxys = mi.Deoxys(aa)
        """
        self.DATA = DEOXYS
        super(Deoxys, self).__init__(aardvark=aardvark)


class Meleotta(bc.I2CMuxInstrument):
    def __init__(self, aardvark):
        """Initialize the I2C multiplexer.

        :param Aardvark aardvark:
            An Aardvark object through which I2C commands are relayed.

        .. code-block:: python

            import microlab_instruments as mi

            aa = mi.Aardvark()
            meleotta = mi.Meleotta(aa)
        """
        self.DATA = MELEOTTA
        super(Meleotta, self).__init__(aardvark=aardvark)


class Aria(bc.TempSensorInstrument):
    def __init__(self, aardvark, mux):
        """Initialize a Sensirion STS21 temperature sensor.

        :param Aardvark aardvark:
            An Aardvark object through which I2C commands are relayed.

        .. code-block:: python

            import microlab_instruments as mi

            aa = mi.Aardvark()
            aria = mi.Aria(aa)
            print aria.read_temp()
        """
        self.DATA = ARIA
        super(Aria, self).__init__(aardvark=aardvark, mux=mux)


class Pirouette(bc.TempSensorInstrument):
    def __init__(self, aardvark, mux):
        """Initialize a Sensirion STS21 temperature sensor.

        :param Aardvark aardvark:
            An Aardvark object through which I2C commands are relayed.

        .. code-block:: python

            import microlab_instruments as mi

            aa = mi.Aardvark()
            pirouette = mi.Pirouette(aa)
            print pirouette.read_temp()
        """
        self.DATA = PIROUETTE
        super(Pirouette, self).__init__(aardvark=aardvark, mux=mux)


class Rayquaza(bc.GPIBInstrument):
    def __init__(self):
        self.DATA = RAYQUAZA
        super(Rayquaza, self).__init__(nickname=self.DATA['nickname'])


class Groudon(bc.GPIBInstrument):
    def __init__(self):
        self.DATA = GROUDON
        super(Groudon, self).__init__(nickname=self.DATA['nickname'])


class Kyogre(bc.GPIBInstrument):
    def __init__(self):
        self.DATA = KYOGRE
        super(Kyogre, self).__init__(nickname=self.DATA['nickname'])


class Kyurem(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = KYUREM
        super(Kyurem, self).__init__(socket_pair=self.DATA['socket'])


class Zygarde(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = ZYGARDE
        super(Zygarde, self).__init__(socket_pair=self.DATA['socket'])
        self.write(':waveform:byteorder msbfirst')
        self.write(':waveform:format word')
        self.write('*OPC')

    def _chop16(self, s):
        """A generator that, given a string, yields its 16-bit slices.

        :param str s:
            The string to be chopped
        :returns out:
            A two-character (16-bit) string.
        :rtype: str
        """
        n = 0
        while True:
            k = s[n:n+2]
            if not k:
                break
            yield k
            n += 2

    def _half_to_float(self, half):
        """Converts half-precision floating-point (16-bit) binary data to
        Python ``float``\ .

        :param str half:
            A 16-bit string to be converted to a Python float
        :returns out:
            The actual floating point number represented by the 16-bit string.
        :rtype: float

        This was copied from `fpmurphy`_

        .. _fpmurphy: http://fpmurphy.blogspot.com/2008/12/half-precision-floating-point-format_14.html
        """
        # Get byte order of input
        bo = '<' if self._is_little_endian() else '>'

        # Preliminary unpacking
        fmt = '{0}H'.format(bo)
        h = unpack(fmt, half)[0]

        # Pad 16 bits to 32 bits
        s = int((h >> 15) & 0x00000001)  # sign
        e = int((h >> 10) & 0x0000001F)  # exponent
        f = int(h         & 0x000003FF)  # fraction
        if e == 0x00:   # exponent is 0
            if f == 0x00:
                hpad = int(s << 31)
            else:
                while not (f & 0x00000400):
                    f <<= 1
                    e -= 1
                e += 1
                f &= ~0x00000400
        elif e == 0x1F:  # exponent is 31
            if f == 0x00:
                hpad = int((s << 31) | 0x7F800000)
            else:
                hpad = int((s << 31) | 0x7F800000 | (f << 13))
        e = e + (127 - 15)
        f = f << 13
        hpad = int((s << 31) | (e << 23) | f)

        # struct.pack hack
        st = pack('I', hpad)
        out = unpack('f', st)
        return out

    def read_preamble(self):
        """Read the waveform preamble from Zygarde.  It contains the following
        metadata about the waveform data:

        :returns out:
        :rtype: dict
        """
        # TODO Combine write, preamble and data in one function
        # TODO Read :waveform:preamble
        #           format WORD this is two bytes for each data point
        #           type   :waveform:type?
        #           points :waveform:points? can be found in the header of :waveform:data?
        #           count  :acquire:count? averaging for one data point, etc
        #           xincrement
        #           xorigin
        #           xreference
        #           yincrement
        #           yorigin
        #           yreference
        # TODO Read :save:waveform:start I do not know how to transfer a file
        pass

    def compose_waveform_xy(self, waveform_y, waveform_preamble):
        """Compose the (x,y) data list according to the y data and preamble
        obtained from the instrument.

        :returns out:
            A 2-column list.  The first column holds the x values and the
            second column holds the y values.
        :rtype: list
        """
        # TODO Read :waveform:data
        #           :waveform:byteorder DONE
        #           :waveform:unsigned  DONE
        #           :waveform:format    DONE
        #           :waveform:source    channel | function | math | pod | bus | sbus
        #           :system:precision
        #           0x0000 hole
        #           0x0001 clipped low
        #           0xFFFF clipped high

        # TODO Need to adjust waveform_x for special values (clipped, etc)
        # TODO Need to adjust waveform_x according to preamble
        # TODO Need to create waveform_y according to preamble
        # TODO Need to compose X and Y values
        pass

    def ask_waveform_data(self):
        """A convenience function to query the waveform preamble and waveform
        data in one call.  Additionally, it also composes the (x,y) data list.

        :returns out:
            A 2-column list.  The first column holds the x values and the
            second column holds the y values.
        :rtype: list
        """
        self.write(':waveform:preamble?')
        waveform_preamble = self.read_preamble()
        self.write(':waveform:data?')
        waveform_y = self.read_ieee754()
        out = self.compose_waveform_xy(waveform_y, waveform_preamble)
        return out


class Dialga(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = DIALGA
        super(Dialga, self).__init__(socket_pair=self.DATA['socket'])
        self.write(':format:data real,32')
        self.write('*OPC')


class Palkia(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = PALKIA
        super(Palkia, self).__init__(socket_pair=self.DATA['socket'])
        self.write(':format:data real,32')
        self.write('*OPC')


class Regigigas(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = REGIGIGAS
        super(Regigigas, self).__init__(socket_pair=self.DATA['socket'])


class Xerneas(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = XERNEAS
        super(Xerneas, self).__init__(socket_pair=self.DATA['socket'])


class Yveltal(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = YVELTAL
        super(Yveltal, self).__init__(socket_pair=self.DATA['socket'])


class Zekrom(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = ZEKROM
        super(Zekrom, self).__init__(socket_pair=self.DATA['socket'])


class Giratina(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = GIRATINA
        super(Giratina, self).__init__(socket_pair=self.DATA['socket'])
        self.write(':format:data real,32')
        self.write('*OPC')


class Reshiram(bc.TCPIPInstrument):
    def __init__(self):
        self.DATA = RESHIRAM
        super(Reshiram, self).__init__(socket_pair=self.DATA['socket'])
