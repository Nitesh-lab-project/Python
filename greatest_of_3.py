# Write a program to find the greatest of 3 numbers entered by the user.
num1=int(input("Enter First Number:"))
num2=int(input("Enter second Number:"))
num3=int(input("Enter Third Number:"))

if(num1>=num2 and num1>=num3):
    print("First Number is largest->",num1)
elif(num2>=num1 and num2>=num3):
    print("Second Number is Largest->",num2)
elif(num3>=num1 and num3>=num2):
    print("Third Number is Largest->",num3)
  

