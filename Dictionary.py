"""
  Write a program to enter marks of 3 subjects from the user
  and store them in dictionary. start with an empty 
  dictionary and add one by one. Use subject name as keys 
  and marks as values

"""


marks1=input("Enter marks of physics:")
marks2=input("Enter marks of chemistry:")
marks3=input("Enter marks of maths:")

dict={}
dict["Physics"]=marks1
dict["Chemistry"]=marks2
dict["Maths"]=marks3
print(dict)


# using update()
dict={}
marks1=input("Enter marks of physics:")
dict.update({"physics":marks1})
marks2=input("Enter marks of chemistry:")
dict.update({"Chemisry":marks2})
marks3=input("Enter marks of maths:")
dict.update({"Maths":marks3})

print(dict)