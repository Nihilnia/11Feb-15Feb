# LAMBDA!

#With 'normal way' we are creating functions like that

def exampleFunc():
    print("Bla bla")
exampleFunc()

#With Lambda

exampleFuncX2 = lambda : print("Bla bLA")
exampleFuncX2()

#ANOTHER EXAMPLE:

def yasamakOldurur(a, b):
    return a + b

print(yasamakOldurur(1, 2))

#With lambda

yasamakOldururX2 = lambda a, b : a + b
print(yasamakOldururX2(2, 3))