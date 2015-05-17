from time import strftime
from math import ceil
import sched, time
import pygame, sys
from pygame.locals import *

def getfibseq(number, fib=[5, 3, 2, 1, 1], seq=[]):
	if number == 0:
		return seq

	i = 0
	while (i < len(fib)) and (fib[i] > number):
		i += 1

	return getfibseq(number - fib[i], fib[i + 1:], seq + [fib[i]])


def and_gate(hourcol, mincol):
	if (hourcol == 'c') and (mincol == 'c'):
		return 'b'
	if (hourcol == 'c') and (mincol == 'w'):
		return 'r'
	if (hourcol == 'w') and (mincol == 'c'):
		return 'g'
	if (hourcol == 'w') and (mincol == 'w'):
		return 'w'


def get_colsquares(hour, minute):
	coldict = {
		0: ['w', 'w', 'w', 'w', 'w'],
		1: ['w', 'w', 'w', 'w', 'c'],
		2: ['w', 'w', 'w', 'c', 'c'],
		3: ['w', 'w', 'c', 'c', 'w'],
		4: ['w', 'w', 'c', 'c', 'c'],
		5: ['w', 'c', 'c', 'w', 'w'],
		6: ['w', 'c', 'c', 'c', 'w'],
		7: ['w', 'c', 'c', 'c', 'c'],
		8: ['c', 'c', 'w', 'w', 'w'],
		9: ['c', 'c', 'w', 'c', 'w'],
		10: ['c', 'c', 'c', 'w', 'w'],
		11: ['c', 'c', 'c', 'c', 'w'],
		12: ['c', 'c', 'c', 'c', 'c']
	}

	i = 0
	result = []
	while i < 5:
		result.append( and_gate(coldict[hour][i], coldict[minute][i]) )
		i += 1
	return result


def gettime():
	hour = int(strftime('%I'))
	minute12 = ceil(int(strftime('%M'))/5.0)
	minute = int(strftime('%M'))
	
	return hour, minute12, minute

def eventloop():
	hour, minute12, minute = gettime()
	tim = get_colsquares(hour, minute12)
	print "time: {0}:{1} ".format(hour, minute12) + "fibsquares: " + str(tim)

def main():
	# while True:
	# 	s = sched.scheduler(time.time, time.sleep)
	# 	s.enter(2, 1, eventloop, ())
	# 	s.run()
	rgbw = {
		'w' : (255, 255, 255),
		'r' : (255, 51, 0),
		'b' : (51, 102, 255),
		'g' : (51, 204, 51),
		'bl': (0, 0, 0)
		}


	pygame.init()
	
	DISPLAY = pygame.display.set_mode((800,800),0,32)
	
	# WHITE=(255,255,255)
	# blue=(0,0,255)

	DISPLAY.fill(rgbw['w'])

	
	while True:
		hour, minute12, minute = gettime()
		colsq = get_colsquares(hour, minute12)

		pygame.draw.rect(DISPLAY, rgbw['bl'], (190, 190, 420, 420))
		pygame.draw.rect(DISPLAY, rgbw[colsq[0]], (200, 200, 400, 400))
		pygame.draw.rect(DISPLAY, rgbw['bl'], (400, 200, 10, 400))
		pygame.draw.rect(DISPLAY, rgbw[colsq[1]], (200, 200, 200, 400))
		pygame.draw.rect(DISPLAY, rgbw['bl'], (200, 400, 200, 10))
		pygame.draw.rect(DISPLAY, rgbw[colsq[2]], (200, 200, 200, 200))
		pygame.draw.rect(DISPLAY, rgbw['bl'], (300, 200, 10, 200))
		pygame.draw.rect(DISPLAY, rgbw[colsq[3]], (310, 200, 90, 100))
		pygame.draw.rect(DISPLAY, rgbw['bl'], (300, 300, 100, 10))
		pygame.draw.rect(DISPLAY, rgbw[colsq[4]], (310, 310, 90, 90))

		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()



if __name__ == '__main__':
	main()