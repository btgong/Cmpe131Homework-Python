def swap_last_item(inputList):
	temp = inputList[0]
	inputList[0] = inputList[len(inputList) - 1]
	inputList[len(inputList - 1)] = temp

	return inputList
