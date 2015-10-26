import microlab_instruments as mi

giratina = mi.Giratina()

def sinpy():
	giratina.write(':format:data real,64')
	giratina.write(':source1:function:mode voltage')
	giratina.write(':source1:voltage:mode list')
	giratina.write(':source1:list:voltage 2,3,4')
	giratina.write(':source1:list:start 1')
	giratina.write(':sens1:current:protection 1E-4')
	giratina.write(':output:state on')
	giratina.write(':initiate (@1)')

sinpy()
