# Lists

#How to create? (There is two way)

# 1 - list() Function

listOne = list("Simulacra")
print(listOne)

# 2 - Without using list() Function

listTwo = [] #here is a empty list

#How to add some items?

# append() Function

listTwo.append("Simulation") #we added 'Simulation' as an item.
print(listTwo)

#Methods of lists?

# append(), pop(), sort()

# pop() Function ("delete the last item from list, or delete a spesific one!")

listThree = ["a", "b", "c"]
listThree.pop() #we deleted the last item of listThree
print(listThree) 

#Now let's delete a spesific item from list.
listThree.pop(0) #we deleted 'a' item from list.
print(listThree)


# sort() Function ("ordering")

# if list is alphabetical, then order as alphabetical
listFour = ["world", "of", "warcraft"]
listFour.sort()
print(listFour)
#or order as reversed
listFour.sort(reverse = True)
print(listFour)

# if list is numeric, then order as small to large
listFive = [3, 66, 4324, 0, 1]
listFive.sort()
print(listFive)
#or order as reversed
listFive.sort(reverse = True)
print(listFive)
print("""Note: If there is various items (int, string, boolean etc.) 
         sort function doesnt work properly, gives TypeError""")