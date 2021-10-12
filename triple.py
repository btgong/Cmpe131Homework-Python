import time

def tripler(func):
	def wrapper():
		for x in range(0, 3):
			func()
	return wrapper
