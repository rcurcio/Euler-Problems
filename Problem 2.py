#!/usr/bin/python

DEBUG = True

def main():
	x = 0
	y = 1
	total = x+y
	while True:
		i = x + y
		if DEBUG: print "%i + %i = %i" % (x, y, i)
		x = y
		y = i

		if DEBUG: print i

		if i % 2 == 0:
			if i < 4000000:
				if DEBUG: print "^^^^^ even"
				total += i
			else:
				break

	return total


if __name__ == "__main__":
	print(main())