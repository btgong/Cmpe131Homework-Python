import time

def calculate_time():
	startTime = time.time()
	time.sleep(2)
	endTime = time.time()
	print("Total time " + str(endTime - startTime))
