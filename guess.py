print("Think a Number between 1 to 100")
ready = input("Are you having a number in your mind: ");

if ready == "yes":
	num1 = 0
	num2 = 100
	gotit = False
	for x in range(7):
		print(8-x, "Chances left")
		number = int((num1+num2)/2)
		responce = input("Is the number {} \n".format(number))
		if responce == "yes":
			gotit = True
			break
		elif responce == "higher":
			num1 = number
		elif responce == "lower":
			num2 = number
		else:
			print("See you later")
			exit()
	if gotit:
		print("Yeah I got the number I Win")
	else:
		print("Unable to guess the number You Win")

	exit()
else:
	print("See you soon")
	exit()

