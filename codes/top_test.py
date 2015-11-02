#!/usr/bin/env python
import microlab_instruments as mi
import time
from random import randint
from array import array
from scanchain import *

aa = mi.Aardvark()

def temperature():
    chen = mi.Chen(aa)
    traxex = mi.Traxex(aa, chen)
    xin = mi.Xin(aa, chen)

    print traxex.read_temp()
    try:
        print xin.read_temp()
    except: print 'xin doesnt work'

def scan_operation(OPERATION):
    SCAN_SELECT_ADDRESS = 0x0F

    if OPERATION == 'peripheral':
    	fpga_write(SCAN_SELECT_ADDRESS,0x02)
    elif OPERATION == 'controller':
    	fpga_write(SCAN_SELECT_ADDRESS,0x01)
    elif OPERATION == 'chain':
    	fpga_write(SCAN_SELECT_ADDRESS,0x03)
    else:
	print 'Error: scan_operation(). Valid arguments are peripheral, core, chain.'

def fpga_write(COMMAND,DATA):
    FPGA_ADDRESS = 0x55
    aa.i2c_write(FPGA_ADDRESS, COMMAND)
    aa.i2c_write(FPGA_ADDRESS, DATA)

def fpga_read(COMMAND):
    FPGA_ADDRESS = 0x55
    bufsize = 1
    aa.i2c_write(FPGA_ADDRESS, COMMAND)
    aa.i2c_read(FPGA_ADDRESS, bufsize)

def peripheral_write(AARDVARK,ARRAY,FIELD,DATA):
    a = scanchain(ARRAY)
    a.update_field(FIELD,DATA)
    SEND = array('B',a.create_array()) 
    scan_operation('chain')		
    RESPONSE = AARDVARK.spi_write(SEND)	
    scan_operation('peripheral')

def memory_write(AARDVARK,ARRAY,FIELD,DATA):
    a = scanchain(ARRAY)
    a.update_field(FIELD,DATA)
    if FIELD == 'min_data' or FIELD == 'max_data' or FIELD == 'time_between':
	a.update_field('mem_we_curr', '1')
    elif FIELD == 'sense_count_out':
	a.update_field('mem_we_sensecount', '1')
    elif FIELD == 'wr_nodeaddr':
	a.update_field('wren_nodeaddr', '1')
    elif FIELD == 'wr_subaddr' or FIELD == 'wr_comm':
	a.update_field('wren_rxdata', '1')
    elif FIELD == 'wr_freq':
	a.update_field('wren_freq', '1')
    elif FIELD == 'sense_rx_out':
	a.update_field('mem_we_senserx', '1')
    else:
	print 'Error: memory_write(). Invalid memory field.'

    SEND = array('B',a.create_array()) 
    scan_operation('chain')		
    RESPONSE = AARDVARK.spi_write(SEND)	
    scan_operation('peripheral')
   
    if FIELD == 'min_data' or FIELD == 'max_data' or FIELD == 'time_between':
	a.update_field('mem_we_curr', '0')
    elif FIELD == 'sense_count_out':
	a.update_field('mem_we_sensecount', '0')
    elif FIELD == 'wr_nodeaddr':
	a.update_field('wren_nodeaddr', '0')
    elif FIELD == 'wr_subaddr' or FIELD == 'wr_comm':
	a.update_field('wren_rxdata', '0')
    elif FIELD == 'wr_freq':
	a.update_field('wren_freq', '0')
    elif FIELD == 'sense_rx_out':
	a.update_field('mem_we_senserx', '0')
    else:
	print 'Error: memory_write(). Invalid memory field.'

    SEND = array('B',a.create_array())
    scan_operation('chain')
    RESPONSE = AARDVARK.spi_write(SEND)
    scan_operation('peripheral')

#PUMP_CAP = 0x00
#STORAGE_CAP = 0x01
#60HZ_OUT = 0x02
#TX_EN = 0x03
#RX_EN = 0x04
#DIGI_EN = 0x05
#BG_ON = 0x06
#DCDC = 0x07 #COMP_EN_IN,EN_CTRL_PADS
#CLK_CONV = 0x08
#TSCS_EN = 0x09 #ENABLE,CLOCK_ENABLE, If 1, TS
#CLK_FILTER = 0x0A
#TX_IN = 0x0B
#RXSIG_INT = 0x0C
#RST_CONTROL = 0x0D
#CLK_CONTROL = 0x0E
#SCAN_CHAIN = 0x0F

while True:
    time.sleep(1)
    try:
	INIT = array('B',[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
	
	#memory_write(aa,INIT,'wr_freq','01010111')
	#scan_operation('chain')
	#RESPONSE = aa.spi_write(INIT)

	#b = scanchain(RESPONSE)
	#b.read_all_fields()

	fpga_write(0x03,0x01)
	fpga_write(0x04,0x01)
	fpga_write(0x05,0x00)
	fpga_write(0x06,0x00)

	#fpga_write(0x09,0x02)
	#fpga_write(0x09,0x03)
	
	fpga_write(0x08,0x01) #turn on the 7.2MHz clock from FPGA
	fpga_write(0x07,0x03) #turn on comp_en_in (bit 1) and en_ctrl_pads (bit 0)
	fpga_write(0x0A,0x01) #turn on 2MHz clock for filter

        #temperature sensor test sequence
	#fpga_write(0x09,0x01)
	#fpga_write(0x09,0x03)
	#time.sleep(1)
	#scan_operation('peripheral')
	#scan_operation('chain')
	#RESPONSE = aa.spi_write(INIT)
	#b = scanchain(RESPONSE)
	#b.read_all_fields()
	#fpga_write(0x09,0x01)
	#time.sleep(1)
	#scan_operation('peripheral')
	#scan_operation('chain')
	#RESPONSE = aa.spi_write(INIT)
	#b = scanchain(RESPONSE)
	#fpga_write(0x09,0x03)
	#time.sleep(1)
	#scan_operation('peripheral')
	#scan_operation('chain')
	#RESPONSE = aa.spi_write(INIT)
	#b = scanchain(RESPONSE)
	#b.read_all_fields()
        #end of temp sensor test

	#current sensor test sequence 
        fpga_write(0x09,0x82) #reset curr sense, enable one shot
	fpga_write(0x09,0x81) #enable curr sense
	time.sleep(.5) #wait for conversion to finish
        scan_operation('peripheral')
        scan_operation('chain')
        RESPONSE = aa.spi_write(INIT) #flush it out
        b = scanchain(RESPONSE)
        b.read_field('current_data')
	b.read_field('current_data_ready')
	#b.read_all_fields()
	
	#end of current sensor test

	#fpga_write(0x02,0x01)
	#fpga_write(0x08,0x01)
	#fpga_write(0x09,0x03)
	#fpga_write(0x0A,0x01)
	#fpga_write(0x0B,0x01)
	fpga_write(0x0C,0x00)
	#fpga_write(0x0D,0x00)
	#fpga_write(0x0E,0x00)

	#peripheral_write(aa,RESPONSE,'en_rx_power','1')

	#temperature()
        #scan_operation('read')
    except Exception as e:
        print e.message

