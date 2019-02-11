# TUPLES

#Tuples are like lists.
#But there is a important difference: You can't make any change to tuples.
#And that's why Tuples more safe then lists.

# How to create?

#There is two way

# 1 - tuple() Function

newTuple = tuple("nihil")
print(newTuple)

# 2 - Without using function

otherTuple = ("N", "o", "r", "d", "a")
print(otherTuple)

# Methods of Tuples

# 1 - count() Function “count any item, how many there?”

print(newTuple.count("i")) #2
total = otherTuple.count("e") #0
print(total)

# 2 - index() Function  “On which index that item?”
print(newTuple.index("l")) #4
#Note: index() function always gives first index of parameter.
print(newTuple.index("i")) #1
#IMPORTANT NOTE: If parameter is not in the tuple, Python gives us an ValueError.