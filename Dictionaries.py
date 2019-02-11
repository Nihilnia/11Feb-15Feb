# DICTIONARIES

# In Python, dictionaries so similar to irl dictionaries.

#How to create? 

# 1 - Using Brackects
exampleDict = {"keyOne": "valueOne", "nihil": 1, 333: "nia"}

# 2 - Using dict() Function
dict2 = dict()
dict2["keyOne"] = "Epica1"
dict2["keyTwo"] = "Epica2"
print(dict2)

#How to use?

print(dict2["keyTwo"], "Cry For The Moon!")

#IMPORTANT NOTE: If there is no key in the list like parameter, Python gives us an ValueError. 

#Change of any variable at Dict?
dict2["keyOne"] = "Epica"
dict2["keyTwo"] = "Cry For The Moon"
print(dict2)

#Methods of Dictionaries?

# keys(), values(), items()

songs = {"Epica": "Cry For The Moon", "David Guetta": "Lovers on the Sun"}

# keys() Function "Get all the keys from the dict"

allKeys = songs.keys()
print("All keys of dict:", allKeys)
print(type(allKeys)) #Notice that!

# values() Function "Get all the values from the dict"

allValues = songs.values()
print("All values of dict:", allValues)
print(type(allValues)) #Notice that too!

# items() Function "Get all the keys and values from the dict"

allItems = songs.items()
print("All items of dict:", allItems)
print(type(allItems)) #And this too!