import random

r = random.randint(0, 100)
while True:
	num = input('Please guess a number: ')
	num = int(num)
	if num == r:
		print('Yes, it is', r)
		break
	elif num < r:
		print('Larger')
	elif num > r:
		print('Smaller')
