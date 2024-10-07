#1st Question
"""
  you are give a list of subjects for students. Assume one classroom is required for 1
  subject. How many classroom are needed by all students.

  'pyhon','java','C++','javascript','java',
  'python','java','C++','C'

"""

set={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(set)
print(len(set))





# 2nd Question
"""
  Figure out a way to store 9 and 9.0 as separate values in the set.
  --> by making string any one number or
  --> pair both with datatype
"""

#By string
set={9,"9.0"}
print(set)

#By pair
set={ ("float",9.0),("int",9)}
print(set)
