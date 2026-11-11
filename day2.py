# name = "Rahul"
# college = "Lakshmi Narain College Of Technology and Science "
# address = "Bhopal"

# # print(name, " " +college," " + address)
# print(name)
# print(college)
# print(address)

# basic operation in string 
# 1. concotaration 

# first = "Hello"
# second = "Rahul"

# print(first + second)
# print(first + " " + second)



# 2. Length of string 

# str = "Lakshmi Narain College Of Technology and Science"

# print(str)
# print(len(str))
# print(type(len(str)))
# print(type(str))

# 3. indexing and Slicing

# name = "Rahul Pawar" 

# print(name[0])
# print(name[0:5])
# print(name[5])
# print(name[0:])

#  4. string Functions

# name = "hello everyone my name is Rahul Pawar"

# print(name.endswith("war"))
# print(name.capitalize())
# print(name.casefold())
# print(name.count("e"))
# print(name.find("Rahul"))
# print(name.replace("Pawar", "Bhadekar"))

# NOTE => This function is return a new string the original string is not change 

#  1. write a program  to input the first name and print its length 

# name = str(input("Enter your first name: "))
# print(len(name))


# 2. write a program to find the occurence of ' $ ' sign in your string 


# str = "hy $ my $ name $ is $ Rahul"

# print(str.count("$"))



# 3. write a program to capitalize the first word of string and input a string 

# name = input("enter string name: ")
# print(name.capitalize())







##### CONDITIONAL STATEMENT 

# light = "yellow"

# if light == "red":
#     print("Stop")
# elif light == "yellow":
#     print("Look")
# elif light == "green":
#     print("Run")
# else:
#     print("light is broken")



# light = input("enter the singnal colore : ")

# if light == "red":
#     print("Stop")
# elif light == "yellow":
#     print("Look")
# elif light == "green":
#     print("Run")
# else:
#     print("light is broken")




# marks = int(input("Enter your marks :" ))

# if marks >= 90:
#     print("Grade : A")
# elif marks >= 80:
#     print("Grade : B")
# elif marks >=70:
#     print("Grade : c")
# elif marks >= 60:
#     pring("Grade : d")
# else: 
#     print("Fail")




# 1. write a program to check the number is enter by the user is even or add

# number = int(input("Enter number: "))

# if number%2 == 0:
#     print("Even number")
# else:
#     print("odd number ")





# 2. write a program to find the gratest of three number entered by the user 

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))

# if num1>num2 and num1>num3:
#     print("number 1 is grater")
# elif num2>num1 and num2>num3:
#     print("number 2 is grater")
# else:
#     print("number 3 is grater")



# 3. write a program to check if the number is given the user is multiple by 7 or not

# num = int(input("enter your number : "))

# if num%7 == 0:
#     print("number is multiple of 7 ")
# else:
#     print("number is not multiple of 7")