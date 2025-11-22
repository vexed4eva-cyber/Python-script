import time
def pause():
	time.sleep(2)
def check_mate():
	if type1.lower() in ["multiply","m"]:
		print(num1 * num2)
		pause()
	elif type1.lower() in ["divide","d","division"]:
		print(num1 / num2)
		pause()
	elif type1.lower() in ["e"]:
		print(num1 ** num2)
		pause()
	elif type1.lower() in ["add","a","addtion"]:
		print(num1 + num2)
		pause()
	elif type1.lower() in ["subtraction","s","minus"]:
		print(num1 - num2)
		pause()

# from lines 4-19 handles the decifering for what operatior they chose and doing the math for it
type1 = input("mutliply,divde,Exponents addtion or subtraction (you can just use the first letter of it) ")
if type1.lower() in ["multiply","m","divide","d","exponents","e","add","addtion","a","subtraction","s"]:
	vaild_input = True
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
else:
	print("remeber that if u cant spell like me just use the first letter")
	vaild_input = False
# And this is validates wheather they correctly put a vaild operator in and makes a funtion named valid_input to remember this

# The below actucaly runs it
if vaild_input == True:
	check_mate()
else:
	quit()