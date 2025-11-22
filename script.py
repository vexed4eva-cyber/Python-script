type1 = input("mutliply,divde,Exponets addtion or subtraction (you can just use the first letter of it) ")
num2 = float(input("Enter first number: "))
num3 = float(input("Enter second number: "))
if type1.lower in ["multiply","m","divide","d","exponets","e","add","addtion","a","subtraction","s"]:
	valid_input = True
if type1.lower in ["multiply","m"]:
	print(num1 * num2)
if type1.lower in ["divide","d","divshion"]:
	print(num1 % num2)
if type1.lower in ["e"]:
	print(num1 ** num2)
