#!python3
#traffic light using itertools and random modules

from time ______ sleep
______ itertools
______ random

colours = 'Red Green Amber'.split()
rotation = itertools.cycle(colours)

___ rg_timer(
	r_ random.randint(5,9)

___ light_rotation(rotation
	___ colour __ rotation:
		__ colour __ 'Amber':
			print('Caution! The light is %s.\n' % colour)
			sleep(5)
		____ colour __ 'Red':
			print('Stop! The light is %s.\n' % colour)
			sleep(rg_timer())
		____
			print('Go! The light is %s.\n' % colour)
			sleep(rg_timer())


__  -n __ '__main__':
	light_rotation(rotation)
