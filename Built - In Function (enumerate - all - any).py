# ENUMERATE

listem = ["Elma", "Armut", "Kiraz"]

for indexNumber, item in enumerate(listem):
        print(indexNumber + 1, item)

listem2 = ["a", "b", "c", "d", "e", "f"]
for indexNumber, item in enumerate(listem2):
        if indexNumber % 2 == 0:
                print(indexNumber, item)



# ALL & ANY


def hepsi(liste):
        for f in liste:
                if not f:
                        return False
        return True

def herhangi(liste):
        for f in liste:
                if f:
                        return True
        return False

myList = [0, 1]


print(hepsi(myList))
print(herhangi(myList))


"WE DON'T NEED TO DO THAT, WE HAVE CUUTEE FUNCTIONS FOR THAT"

theList = [True, 0, False, 1]
theList2 = [True, 1, True]
theList3 = [False, 0, False, False]

print(all(theList)) #False
print(any(theList2)) #True
print(any(theList3)) #False