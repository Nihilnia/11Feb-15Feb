# ERROR HANDLING!

""" Use try blocks for where could run as wrong """
""" Use except blocks for what will be happen if somethings gone wrong """
""" Use rais blocks for create a error like Python style and give message to user."""

try:
    userInput = int(input("Give me a number: "))
    print("Cong! LMAO")
except ValueError:
    print("You should give me a number.")


#Raise

trChars = "ıöÖçÇşğĞİ"
userName = input("Username: ")
for chars in userName:
    if chars in trChars:
        raise ValueError("Turkish chars not allowed!")
else:
    print("Welcome", userName)