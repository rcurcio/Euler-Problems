
DEBUG = False

def main():

	for i in xrange(10000000, 1000000000):
		if DEBUG:
			print(i)
			print('^^^^ i')

		for j in xrange(20, 0, -1):
			if DEBUG:
				print(j)
				print('^^^ j')

			if i % j == 0:
				smallest = i 
				if j == 1:
					return smallest

			else:
				break

print(main())