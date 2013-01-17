DEBUG = True


def multiply3digitNumbers():
	# Multiplying all three digit numbers to get a palindrome.

	secondPali = list()

	for i in xrange(999, 99, -1):


		for j in xrange(999, 99, -1):


			pali = i * j
			if DEBUG:
				print(pali)
				print('^^^^^ pali')
	
			pali = list(str(pali))
        	
			secondPali = pali

			pali = ''.join(pali)

			secondPali.reverse()

			secondPali = ''.join(secondPali)

			if pali == secondPali:
				return pali

			else:
				break

multiply3digitNumbers()
		


