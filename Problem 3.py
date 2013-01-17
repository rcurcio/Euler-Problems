
DEBUG = False

import sys

def getLargeFactors():
	factor = 2
	print('What number would you like to find the largest prime factor?')
	NUMBER = int(input())
	largestFactor = 1
	answer = NUMBER
	while answer - factor >= 0:
		# dividing our number by a large factor.
		answer = answer / factor

		if answer - round(answer) == 0:
			# To see if the number = 0, if it does, then it is a factor.
			largestFactor = factor
			if DEBUG:
				print(largestFactor)
				print('^^^^ largestFactor')
		else:
			answer *= factor
			factor += 1
			if DEBUG:
				print(answer)
				print('^^^^ answer')
				print(factor)
				print('^^^^ factor')

	return largestFactor  



def playAgain():
	# Ask if they would like to try again.
	print('Would you like to play again? Yes or No')
	return input().lower().startswith('y')

while True:
	print(getLargeFactors())
	if not playAgain():
		sys.exit()
		
