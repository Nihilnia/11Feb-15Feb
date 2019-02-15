#  FILE OPERATIONS

"""
w - write
a - append
r - read
"""

"HOW TO OPEN A FILE?"
""" open("fileName.extension, "mode", encoding = "bla-BLA) """


myFile = open("takeTheBluePill.txt", "a", encoding = "utf-8")
if myFile:
    print("File Created!")
else:
    print("File not created!")
myFile.write("""You take the blue pill - the story ends, you wake up in your bed and believe whatever you want to believe. 
You take the red pill - you stay in Wonderland and I show you how deep the rabbit-hole goes.""")

myFile.close()

userChoice = input("Wanna read your file?")
if userChoice == "yes":
    readMyFile = open("takeTheBluePill.txt", "r", encoding = "utf-8")
    content = readMyFile.read()
    print(content)
    readMyFile.close()
else:
    print("See ya!")
