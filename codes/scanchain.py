#
#
# To use:
# 	Add the following line at the beginning:
#	from scanchain import *
#
# To create a variable:
#	variable_name = scanchain(variable_holding_the_raw_array)
#
# To update a field:
#	variable_name.update_field("field_name", "new_value")
#
# To get the array again with all the updated fields:
#	variable_for_updated_array = variable_name.create_array()
#

class scanchain(object):
	def __init__(self, scan_array):
		scan_array_cc = ''.join(format(x, '08b') for x in scan_array)

		self.fields = ('state', 'reset_delay', 'timeslot', 'rx_state', 'freq_state', 'phase_state', 'pr_valid', 'f_lock', 'sync_timeout', 'sync_err', 'curr_state', 'ag_state', 'tx_state', 'txout', 'txout_bar', 'mem_we_temp', 'mem_we_senserx', 'sense_rx_out', 'mem_we_sensecount', 'sense_count_out', 'wren_nodeaddr', 'wr_nodeaddr', 'wren_rxdata', 'wr_comm', 'wr_subaddr', 'wren_freq', 'wr_freq', 'mem_we_curr', 'max_data', 'min_data', 'time_between', 'en_rx_power', 'en_tx_power', 'controller_sleep', 'en_dcdc', 'en_ct_switch', 'en_curr_temp', 'rxsig_int', 'por_ready_tx', 'por_ready_rx', 'clk_120', 'por_ready_dcdc', 'rd_timeb', 'rd_minc', 'rd_maxc', 'rd_freq', 'rd_subaddr', 'rd_comm', 'rd_nodeaddr', 'rd_sense_count', 'rd_sense_or_rx', 'rd_temp', 'temp_data_ready', 'temp_ind_out', 'temp_dep_out', 'current_data', 'current_data_ready', 'force_state')

		self.bits = [(4,0), (2,0), (2,0), (3,0), (3,0), (3,0), (1,0), (1,0), (1,0), (1,0), (2,0), (2,0), (4,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (6,0), (1,0), (7,0), (1,0), (3,0), (7,0), (1,0), (8,0), (1,0), (8,0), (8,0), (8,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0), (8, -1), (8, -1), (8, -1), (8, -1), (7, -1), (3, -1), (7, -1), (6, -1), (1,0), (8, -1), (1,0), (10,0), (10,0), (8, -1), (1,0), (1,0)]

		self.parsed_data = {}

		i = 0
		bit_start = 0
		while i < 58:
			if self.bits[i][1] == -1:
				self.parsed_data[self.fields[i]] = scan_array_cc[bit_start+self.bits[i][0]-1:bit_start-1:-1]
			else:
				self.parsed_data[self.fields[i]] = scan_array_cc[bit_start:bit_start+self.bits[i][0]]
			#print fields[i], parsed_data[fields[i]]
			bit_start = bit_start + self.bits[i][0]
			i = i + 1

	def update_field(self, field="x", value="x"):
		if field == "x" or value == "x":
			print "Usage: <object variable>.update_field('field string', 'field value')"
			return

		if field not in self.fields:
			print "Error: %s not a valid field." % field
			return
		self.parsed_data[field] = value

	def read_field(self, field="x"):
		if field == "x":
			print "Usage: <object variable>.read_field('field string')"
			return

		if field not in self.fields:
			print "Error: %s not a valid field." % field
			return

		print "%s =" % field, self.parsed_data[field]

	def read_all_fields(self):
		
		for field in self.fields:
			print "%s =" % field, self.parsed_data[field]
		

	def create_array(self):
		i = 0
		rearranged = ''
		while i < 58:
			if self.bits[i][1] == -1:
				rearranged = rearranged + self.parsed_data[self.fields[i]][::-1]
			else:
				rearranged = rearranged + self.parsed_data[self.fields[i]]
			i = i + 1

		new_data = []
		j = 0
		i = 7
		for bit in rearranged:
			if i == 7:
				new_data.append(0)
			if bit == '1':
				new_data[j] = new_data[j] | (1 << i)
			i = i - 1
			if i == -1:
				i = 7
				j = j + 1

		return new_data

# for reference purposes
	# output of the controller going to the peripherals
	#state = scan_out[0:4]
	#reset_delay = scan_out[4:6]
	#timeslot = scan_out[6:8]
	#rx_state = scan_out[8:11]
	#freq_state = scan_out[11:14]
	#phase_state = scan_out[14:17]
	#pr_valid = scan_out[17]
	#f_lock = scan_out[18]
	#sync_timeout = scan_out[19]
	#sync_err = scan_out[20]
	#curr_state = scan_out[21:23]
	#ag_state = scan_out[23:25]
	#tx_state = scan_out[25:29]
	#txout = scan_out[29]
	#txout_bar = scan_out[30]
	#mem_we_temp = scan_out[31]
	#mem_we_senserx = scan_out[32]
	#sense_rx_out = scan_out[33]
	#mem_we_sensecount = scan_out[34]
	#sense_count_out = scan_out[35:41]
	#wren_nodeaddr = scan_out[41]
	#wr_nodeaddr = scan_out[42:49]
	#wren_rxdata = scan_out[49]
	#wr_comm = scan_out[50:53]
	#wr_subaddr = scan_out[53:60]
	#wren_freq = scan_out[60]
	#wr_freq = scan_out[61:69]
	#mem_we_curr = scan_out[69]
	#max_data = scan_out[70:78]
	#min_data = scan_out[78:86]
	#time_between = scan_out[86:94]
	#en_rx_power = scan_out[94]
	#en_tx_power = scan_out[95]
	#controller_sleep = scan_out[96]
	#en_dcdc = scan_out[97]
	#en_ct_switch = scan_out[98]
	#en_curr_temp = scan_out[99]

	# input of the controller from the peripherals
	#rxsig_int = scan_out[100]
	#por_ready_tx = scan_out[101]
	#por_ready_rx = scan_out[102]
	#clk_120 = scan_out[103]
	#por_ready_dcdc = scan_out[104]
	#rd_timeb = scan_out[112:104:-1]
	#rd_minc = scan_out[120:112:-1]
	#rd_maxc = scan_out[128:120:-1]
	#rd_freq = scan_out[136:128:-1]
	#rd_subaddr = scan_out[143:136:-1]
	#rd_comm = scan_out[146:143:-1]
	#rd_nodeaddr = scan_out[153:146:-1]
	#rd_sense_count = scan_out[159:153:-1]
	#rd_sense_or_rx = scan_out[160]
	#rd_temp = scan_out[168:160:-1]
	#temp_data_ready = scan_out[169]
	#temp_ind_out = scan_out[170:180]
	#temp_dep_out = scan_out[180:190]
	#current_data = scan_out[197:189:-1]
	#current_data_ready = scan_out[198]
	#force_state = scan_out[199]

