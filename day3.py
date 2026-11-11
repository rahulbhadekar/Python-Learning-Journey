#####     LIST IN PYTHON    ######

# A list is a built-in data type that stores the collection of values in sequer bracket [ ]. 
# A list can store a elements in diffrent types(integer, float, string etc.)


# marks = [87, 84, 79, 88, 99, 94]

# student = [ "Rahul", 23, "Bhopal"]

# print(marks)
# print(student)

# print(marks[2])
# print(student[0])

# print("Student Physics marks : ", + marks[3])
# print("Student city name : " + student[2])


# LIST IS MUTABLE IN PYTHON 

# student = [ "Rahul", 23, "Bhopal"]

# student[0] = "Rahul_Pawar"
# #########  student[3] = "LNCT"          # NOTE- BCZ THIS LIST LENGTH IS  2 INDEX ND WE ADD 3 THAT WHY ITS GIVE A ERROR 

# print(student)
# print(len(student))





#### ------ LIST SLICING -------


# marks = [87, 84, 79, 88, 99, 94]

# print(marks[0:2])
# print(marks[:3])
# print(marks[0])            # its provide a indexing value not slicing value 
# print(marks[0:])
# print(marks[2:5])
# print(marks[-5:-1])



# --------------  LIST METHOD ------------


# marks = [87, 84, 79, 88, 99, 94]

# marks.append(90)
# print(marks)

# marks.sort()
# print(marks)

# marks.count(1)
# print(marks)

# marks.insert(0, 80)
# print(marks)

# marks.remove(87)
# print(marks)

# marks.pop(1)
# print(marks)

# marks.reverse()
# print(marks)

# marks.sort(reverse=True)
# print(marks)



# -----------  TUPLE  ----------

# A tuple is a built in data type that stores an immutable sequence of value in rounf brackets ( ). once created its can not be changed.

# tup = (87, 84, 79, 88, 99, 94)
#                              #  sliching are alowed
# print(tup[0])
# print(tup[0:4])
# print(tup[1:3])
# print(len(tup))

# sum = tup[0] + tup[1]
# print(sum)



# --- tuple creating ---

# tup1 = ()
# tup2 = (2)                    #its not tuple bcz elements after , requred 
# tup3 = (3,)
# tup4 = (8, 4, 5, 6,)

# print(type(tup2))
# print(type(tup3))
# print(len(tup4))

# print(len(tup1))
# print(len(tup3))




# -----------TUPLE METHOD----------

# tup = (1, 2, 3, 1, 4)

# print(tup.index(2))             # PRINT INDEX 2 VALUE
# print(tup.count(1))             # COUNT THE NUMBER IN TUPLE



#  Ask the user tp the enter the name of fav movies and store in the list

# movies =[]

# movies.append(input("Enter fisrt fav movie name : "))
# movies.append(input("Enter second fav movie name : "))
# movies.append(input("Enter third fav movie name : "))

# print(movies)





# check if a list is a palindrome (read forword and backword is same )

# num = [1, 2, 3, 2, 1]

# copy_num = num.copy()
# copy_num.reverse()

# if num == copy_num:
#     print("palindrome")
# else:
#     print("not a palindrome")






#  count the nummber of students the " A " grade in the following tuple 

# grade = ("C", "D", "A", "A", "B", "B", "A")

# print(grade.count("A"))



