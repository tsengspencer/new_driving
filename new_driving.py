place = input("where are you from?")
age = int(input("what's your age?"))
if place == "Taiwan":
   if age >= 18:
   		print ("You are allowed to drive if you have a license")
   else:
    	print("Sorry! You are able to drive, according to the law.")

elif place == "USA":
 	if age < 16:
 		print("You cannot drive!")
 	else: 
 		print("No worries! You are allowed to drive.")
