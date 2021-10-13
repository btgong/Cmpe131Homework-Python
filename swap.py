def swap_last_item(inputList):
	'''
	Returns a list with swapped first and last elements

		Parameters:
			inputList (list): A list of integers

		Returns:
			inputList (list): A list of swapped first and last elements
	'''
	# Need a temp variable to temporarily hold first element
	temp = inputList[0]
	inputList[0] = inputList[len(inputList) - 1]
	inputList[len(inputList) - 1] = temp

	return inputList
