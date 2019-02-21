"""

EXERCISES FOR BUILT - IN FUNCTIONS 

"""


#MAP FUNCTION ("DO IT FOR EVERY ITEM")
"DO NOT FORGET: MAP FUNCTION RETURN A 'MAP' OBJECT"

mapOne = list(map(lambda x, y : x + y,   [1, 2, 3], [4, 5, 6]))
print("mapOne:", mapOne)

mapTwo = tuple(map(lambda x : x + 2, [1, 2, 3]))
print("mapTwo:", mapTwo)


#REDUCE FUNCTION("DO IT FOR FIRST TWO ITEM, AND AFTER CONTINUE TO 3-4-5...")

from functools import reduce

#An example for factorial..
reduceOne = reduce(lambda x, y : x * y, range(1, 6)) #120
print("reduceOne:", reduceOne) 

def exampleKK(x, y):
    return x + y - 2

reduceTwo = reduce(exampleKK, [2, 3, 4, 5]) #8
print("ReduceTwo:", reduceTwo)


#FILTER FUNCTIN("DO IT FOR EVERY ITEM, BUT FIRST PARAMETER SHOULD BE BOOLEAN")

def evenOrNot(x):
    if x % 2 == 0:
        return x

filterOne = list(filter(evenOrNot, range(11))) #0, 2, 4, 6, 8
print("filterOne:", filterOne)

def primeNumber(x):
    aList = []
    for f in range(1, x + 1):
        if x % f == 0:
            aList.append(f)
    
    if len(aList) < 3:
        return True

primeNumberResult = list(filter(primeNumber, range(2, 101)))
print("p RESULT:", primeNumberResult)

# ZIP FUNCTION("GROUPING")

listOne = [1, 2, 3]
listTwo = [4, 5, 6]

groupIt = list(zip(listOne, listTwo))
print(groupIt)


for first, second in zip(listOne, listTwo):
    print("first:", first, "second:", second)

another = ["Python", "Discord", "Spotify", "Nihil"]
for number, item in zip(range(1, len(another) + 1), another):
    print(number, item)