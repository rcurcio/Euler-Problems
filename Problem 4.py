DEBUG = True

def multiply3digitNumbers():
	# Multiplying all three digit numbers to get a palindrome.

	secondPali = list()

	p = 999

	while p > 99:

		n = 999

		while n > 99:

			pali = p * n
			if DEBUG:
          			print(pali)

			n -= 1
	
			pali = list(str(pali))
        	
			secondPali = pali

			pali = ''.join(pali)

			secondPali.reverse()

			secondPali = ''.join(secondPali)

			if pali == secondPali:
				print(pali)
				print('pali')
			else:
				break


			


multiply3digitNumbers()
		


