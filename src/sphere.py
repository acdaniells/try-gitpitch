import sys
import math

def sphere_volume(r):
	"""Calculate the volume of a sphere with radius r."""
	return 4/3. * math.pi * r ** 3

if __name__ == '__main__':
    print(sphere_volume(float(sys.argv[1])))
