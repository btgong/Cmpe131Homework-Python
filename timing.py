import time

def calculate_time(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		print("Total time " + str(endTime - startTime)
	return wrapper
		
