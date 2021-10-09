import time

def calculate_time(func):
	def wrapper():
		startTime = time.time()
		func()
		endTime = time.time()
		funcTime = str(endTime - startTime)
		print("Total time " + funcTime)
	return wrapper
		
