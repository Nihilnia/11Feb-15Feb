# Area Of Rectangle

def areaRe(tuplex):
        return tuplex[0] * tuplex[1]

liste = [(3,4),(10,3),(5,6),(1,9)]

results = list(map(areaRe, liste))
print(results)





# Is it a triangle or not?

values = [(3,4,5),(6,8,10),(3,10,7)]

def isItTriangle(x):
        a = x[0]
        b = x[1]
        c = x[2]
        if a < b + c and a > abs(b - c):
                return True
        return False

resultz = list(filter(isItTriangle, values))
print(resultz)


# Even numbers

from functools import reduce

listZ = [1,2,3,4,5,6,7,8,9,10]
def evenNumbers(x):
        if x % 2 == 0:
                return True
        return False

evenOnes = list(filter(evenNumbers, listZ))
totalZ = reduce(lambda x, y : x + y, evenOnes)
print(totalZ)


# For ZIP

names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for n, s in zip(names, surnames):
        print(n, s)
