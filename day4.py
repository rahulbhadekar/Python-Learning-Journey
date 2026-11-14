# #  -----------------  DICTIONARY IN PYTHON  ------------------

# # Dictionary store the data in key : value pairs , witten inside curly brackets { }. 1.Mutable 2.No Duplicate vakues is allowed

info = {
    "name" : "Rahul",
    "cgpa" : 7.5,
    "marks" : [70, 75, 80]
}

print(info["name"])
print(info["cgpa"])
print(info["marks"])

# # dict_name["key"] = value to change exsiting value or add a new pair 

info["cgpa"] = 9.0
info["city"] = "Bhopal"

print(info)


# NESTED DICTIONARY 

student = {
    "name" : "Rahul",
    "score" : {
        "chem" : 98,
        "phys" : 99,
        "math" : 97,
    },
}

print(student["score"])
print(student["score"]["math"])


# DICTIONARY METHOD 

emp = {
    "name" : "Rahul",
    "salary" : 50000
}

print(emp.keys())
print(emp.values())
print(emp.items())
print(emp.get("name"))
print(list(emp.keys()))

emp.update({"city": "Bhopal" , "salary": 60000})

print(emp)