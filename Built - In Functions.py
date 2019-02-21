# Some built-in Functions - 2

"FILTER FUNCTION!"

def primeNumber(x):
    numbersList = list()
    for numbers in range(1, x):
        if x % numbers == 0:
            numbersList.append(x)
    if len(numbersList) == 1:
        return True

#Prime numbers 1 to 1000:
allPrimeNumbers = list(filter(primeNumber, range(1, 1001)))
print(allPrimeNumbers)


"ZIP FUNCTION (HUGEEE!)"


liste1 = [1, 2, 3, 4 , 5]
liste2 = [6, 7, 8, 9, 10, 11]

key = 0

yeniListe = []

while key < len(liste1) and key < len(liste2):
    yeniListe.append((liste1[key], liste2[key]))
    key += 1

print(yeniListe)

#NOW, TAKE A LOOK

newList = list(zip(liste1, liste2))
print("New list:", newList)


#Another example


for x, y in zip(liste1, liste2):
    print("X:", x, "Y:", y)


#Another one

xList = ["Python", "Nihil", "Wow", "Void"]
yList = list(range(1, len(xList) + 1))

for x, y in zip(yList, xList):
    print(x, y)