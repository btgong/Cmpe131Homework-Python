import time

def tripler(func):
	'''
	Decorator that calls function three times.

		Parameters:
			func (function): A function

		Returns:
			wrapper (function): Function that is called
	'''
	def wrapper():
		'''
		Calls function three times.

		Parameters:
			None

		Returns:
			None
		'''
		# Cannot write func() three times, must use loop
		for x in range(0, 3):
			func()
	return wrapper
