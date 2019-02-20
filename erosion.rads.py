#!/usr/bin/python
#
#
import math

# erosion region grows by 50 square miles annually`
changeInArea = 50
scalingFactor = 2 * changeInArea / math.pi

def timeToErosion(distanceFromCenter):
	return int(math.ceil(distanceFromCenter ** 2 / scalingFactor))

if __name__ == '__main__':
	print timeToErosion(0)
	print timeToErosion(1)
	print timeToErosion(25)