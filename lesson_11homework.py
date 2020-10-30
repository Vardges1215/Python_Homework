#Lesson 11
import random
import logging

while True:
	i = random.randint(0,50)
	print(i)
	logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)

	if i < 10:
		logging.debug('this is a Debug message')
	

	elif i > 9 and i < 20:
		logging.info("This is an info message")
	

	elif i > 19 and i < 30:
		logging.warning("This is a warning message")
	

	elif i > 29 and i < 40:
		
		logging.error('This is an error message')


	elif i > 39:
		logging.critical('This is a critical message')
	break

