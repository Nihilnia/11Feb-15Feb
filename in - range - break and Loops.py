# Before start the Loops, let's remember two beautiful things:

# in operand

userName = input("What is your name: ")

if "i" in userName:
    print("Welcome!")
else:
    print("Get out here!")


# range() Function
#That function gives us a number between parameters.

#For LOOP!

print("Even numbers until 40 (with FOR LOOP)")
for evenNumbers in range(41):
    print(evenNumbers)

#While LOOP!

print("40 Pieces \"Simulation\"")
key = 1
while key < 41:
    print(key, ".Simulation", sep = "")
    key += 1

#break Expression!
# if you wanna stop a loop, use break, simple!

forStop = 10
while True:
    print("Erkin Koray")
    forStop += 1
    if forStop == 20:
        break