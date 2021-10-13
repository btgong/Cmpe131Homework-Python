def calculator(number1, number2, operator):
	'''
	Returns the calculation of two decimal numbers with the given operator

		Parameters:
			number1 (float): A decimal integer
			number2 (float): Another decimal integer)
			operator (string): Math operation operator

		Returns:
			Calculation of number1 and number2 with the given operator
	'''
	# Check which operator to use.
	if operator in ('+','-','*','/','//','**'):
		if operator == "+":
			return number1 + number2
		elif operator == "-":
			return number1 - number2
		elif operator == "*":
			return number1 * number2
		# Dividing by 0 is undefined.
		elif operator == "/" and number2 != 0:
			return number1 / number2
		# Dividing by 0 is undefined.
		elif operator == "//" and number2 != 0:
			return number1 // number2
		elif operator == "**":
			return number1 ** number2
		else: return False
	# Terminate if invalid operator is given.
	else: return False

def parse_input():
	'''
	Parses user's equation input and calculates.

		Parameters:
			None

		Returns:
			None
	'''
	# Takes user input
	equation = input("Enter equation")
	# To be able to use in calculator()
	list = equation.split( )
	print(calculator(float(list[0]), float(list[2]), list[1]))
