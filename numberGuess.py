print("Think of a number between 1 to 1000 and i will guess it in 7 chances")

i = 0
lower = 0
higher = 1000

while i < 10:
	ans = input("Is your number {} \n".format((lower+higher)//2))
	if ans.lower()=="yes":
		print("I gueesed the number")
		break
	elif ans.lower() == "higher":
		lower = (lower+higher)//2
	elif ans.lower() == "lower":
		higher = (lower+higher)//2
	else:
		i-=1
		print("Enter a vaild command")
		print("yes")
		print("lower")
		print("higher")
	i+=1

if i == 10:
	print("i am not able to guess the number")