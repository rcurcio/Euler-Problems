
DEBUG = True

def getLargeFactors():
	
	NUMBER = 6008514
	
	largestFactor = 1

	answer = NUMBER

	for i in xrange(2, NUMBER/2):
		while answer % i == 0:

			answer = answer / i
			if DEBUG:
				print('answer = %s' % (answer))

			if answer - round(answer) == 0:

				largestFactor = i

			else:
				answer *= i
				break

	return largestFactor  



print(getLargeFactors())
		
