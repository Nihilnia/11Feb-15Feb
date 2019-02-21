# Some built-in Functions

"MAP FUNCTION!"
# map(function, variable/variables 'list, tuple..')

def double(x):
    return x ** 2

result = list(map(double, [1, 2, 3]))
print("Result 1:", result)

result2 = list(map(double, range(1, 4)))
print("Result 2:", result2)

result3 = list(map(lambda x, y, z : x + y - z, [1, 2, 33], [3, 4], [5, 6]))
print("Result 3:", result3) # -1, 0


"REDUCE FUNCTION!"
from functools import reduce

# reduce(function, variable/variables 'list, tuple..')

def someThings(x, y):
    return x + y

result4 = reduce(someThings, [1, 2, 3])
print("Result 4:", result4)

def biggestNumberInTheList(x, y):
    if x > y:
        return x
    else:
        return y

result5 = reduce(biggestNumberInTheList, [1, 2, 3, 4, 5, 900, 1001])
print("Biggest number in the list:", result5)

# A GOOD EXAMPLE WITH REDUCE: FACTORIAL

userInput = int(input("Which number's factorial you wanna learn: "))
factorial = reduce(lambda number1, number2 : number1 * number2, range(2, userInput + 1))
print(factorial)