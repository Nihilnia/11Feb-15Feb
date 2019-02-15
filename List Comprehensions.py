# LIST COMPREHENSIONS!

listOne = [numbers for numbers in range(0, 11, 2)]
listTwo = [numbers - 1 for numbers in listOne]

print("-- List One --", listOne, sep = "\n")
print("-- List Two --", listTwo, sep = "\n")

#Another example:

numbers = list(range(11))
oddNumbers = [oddOnes for oddOnes in numbers if oddOnes % 2 != 0]
evenNumbers = [evenOnes for evenOnes in numbers if evenOnes % 2 == 0]

print("-- Odd Numbers --", oddNumbers, sep = "\n")
print("-- Even Numbers --", evenNumbers, sep = "\n")


# Even numbers between 1 - 100:

oneToHundred = [evvvv for evvvv in range(101) if evvvv % 2 == 0]
print(oneToHundred)

#or 

oneToHundredX2 = [awwww for awwww in range(0, 101, 2)]
print(oneToHundredX2)

# Last example for now

channelList = {"Channel 1": "TV 1", "Channel 2": "TV 2", "Channel 3": "TV 3"}

channelNumbers = [numbers for numbers in channelList.keys()]
channelNames = [names for names in channelList.values()]

print("-- Channel Numbers --", channelNumbers, sep = "\n")
print("-- Channel Names --", channelNames, sep = "\n")