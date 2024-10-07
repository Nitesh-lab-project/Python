#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  del x
  print("Python is " + x)

myfunc()

print("Python is " + x)



#2nd Method
def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

