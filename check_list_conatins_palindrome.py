# Write a program to check if a list contains a palindrome of elements.
 #Palindrome --> same from both left and right side
  # [1,2,3,2,1]

# if we reverse the copy list is same as original list then its contain palindrome


l1=[1,2,3,2,1]
l2=l1.copy() #copy of original list
l2.reverse()
print(l2)

if(l2==l1):
    print("Palindrome")
else:
    print("Not Palindrome")


l1=[1,2,3]
l2=l1.copy() #copy of original list
l2.reverse()
print(l2)

if(l2==l1):
    print("Palindrome")
else:
    print("Not Palindrome")
