#WAP to input users first name and  print it's length

userName = input("Please enter your name: ")

userNameLength = len(userName)
print(userNameLength)


#WAP to find the occurance of a in the user name input

userName = input("please enter your name: ")

userNameVowels = userName.find("a")

print(userNameVowels)


#WAP to check if a number entered by the user is even or odd

userNumber = int(input("Please enter a number: " ))

if (userNumber % 2 == 0): 
    print("Entered number is an even number.")
else:
    print("Entered number is an odd number.")


#Or..........

userNumber = int(input("Please enter a number: " ))

if (userNumber % 2 != 0):
    print("Entered number is an odd number.") 

else: 
    print("Entered number is an even number.")

#WAP to find the greatest number of the three numbers provided by the user 

userFirstNumber = int(input("Please enter first number: " ))
userSecondNumber = int(input("Please enter second number: " ))
userThirdNumber = int(input("Please enter third number: " ))

if (userFirstNumber > userSecondNumber and userFirstNumber > userThirdNumber):
    print ("First Number is greater than second and Third")
elif (userSecondNumber > userThirdNumber and userSecondNumber > userThirdNumber):
    print("Second Number is Greatest Number")
else: 
    print("Third Number is Greatest Number")

#WAP to check if a number is a multiple of 7 or not

userNumber = int(input("Please enter the number: " ))

if (userNumber % 7 == 0): 
    print("The number is a multiple of 7.")
else: 
    print("The number is not a multiple of 7.")