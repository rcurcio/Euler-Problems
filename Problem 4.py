DEBUG = True


def multiply3digitNumbers():
	# Multiplying all three digit numbers to get a palindrome.

	secondPali = list()

	for i in xrange(999, 99, -1):
		if DEBUG:
			print(i)
			print('i')

		for j in xrange(999, 99, -1):
			if DEBUG:
				print(j)


			pali = i * j

			pali = list(str(pali))
        	
			secondPali = pali

			pali = ''.join(pali)

			secondPali.reverse()

			secondPali = ''.join(secondPali)

			if pali == secondPali:
				return pali

print(multiply3digitNumbers())
		


