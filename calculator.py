def calculator(number1, number2, operator):
	if operator in ('+','-','*','/','//','**'):
		if operator == "+":
			return number1 + number2
		elif operator == "-":
			return number1 - number2
		elif operator == "*":
			return number1 * number2
		elif operator == "/" and number2 != 0:
			return number1 / number2
		elif operator == "//" and number2 != 0:
			return number1 // number2
		elif operator == "**":
			return number1 ** number2
		else: return False
	else: return False

def parse_input():
	equation = input("Enter equation")
	list = equation.split( )
	print(calculator(float(list[0]), float(list[2]), list[1]))
