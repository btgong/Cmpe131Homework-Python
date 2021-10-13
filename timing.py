import time

def calculate_time(func):
	'''
	Decorator that returns time taken for function to run.

		Parameters:
			func (function): A function

		Returns:
			wrapper (function): Computes a function's time to run
	'''
	def wrapper():
		'''
		Calculates and prints time taken for a function to run.

			Parameters:
				None

			Returns:
				None
		'''
		# Calculate time before function to find difference
		startTime = time.time()
		func()
		# Calculate time after function to find difference
		endTime = time.time()
		funcTime = str(endTime - startTime)
		print("Total time " + funcTime)
	return wrapper

