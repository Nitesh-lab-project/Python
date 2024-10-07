#Set Datatype
#represent data not in any order

set={"A","B","C"}
print(set)

#Add new Value in set
set.add("Nitesh")
print(set)

#Remove elements from set
set.remove("C")
print(set)

#Frozenset 
a=frozenset(set)
for i in a:
  print(i)