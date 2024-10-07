#String Datatype

a='Nitesh'   # Single Quotes
print(a)

b="Nitesh"   # Double Quotes
print(b)

c="""Nitesh"""  # Triple Quotes
print(c)



# Add or combine two string
a='Nitesh'
b='Vishwakarma'
print(a+b) #No space between two combine string

#print(a,b) #space between combine string
print(a*2) # repete string 



#Slicing and indexing
#indexing
s="My first project"
print(s[1])  # outpu = y

#slicing
s="My first Project"
print(s[1:5])  #output = y fi


#Most Important string method

x="This is a Good Language"

# 1st 
#strip() --> remove whitespace
print(x.strip())

# 2nd
# lower() -->for lowercase
print(x.lower())

# 3rd 
# upper() --> for uppercase
print(x.upper())

# 4th
# startswith --> check that provide string or word is present in initial on string or not
print(x.startswith("This"))

# 5th
# endswith --> check that provide string or word is present in last or end  on string or not
print(x.endswith("Language"))

# 6th
# find() --> Match index of string
print(x.find("Good"))

# 7th
# replace()
print(x.replace("This","Python"))

# 8th
# join() --> to print symols also by given data i list 
print(",".join(["A","B","C"]))

# 9th
# len() --> length of string
print(len(x))






