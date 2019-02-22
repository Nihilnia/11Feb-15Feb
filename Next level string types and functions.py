# upper() and lower()

print("python".upper())

print("PYTHON".lower())


# replace() Function

stringX = "aaaa bbbbb ccccc"
print(stringX.replace("a", "x"))

stringY = "dreams dreams dreams"
print(stringY.replace("dreams", "Nihil"))


# startswith() & endswith()

"return True or False"

nickName = "Nihil"
print(nickName.startswith("n")) #False
print(nickName.startswith("N")) #True

userInput = input("Give me your name: ")

if userInput.startswith("a"):
    print("Your name starts with 'a'!")
elif userInput.startswith("b"):
    print("Your name starts with 'b'!")
else:
    print("Your name not starts with a or b!")

#OR YOU CAN DO IT MORE SPESIFIC!

if userInput.lower().startswith("a"):
    print("Your name starts with 'a'!")
elif userInput.lower().startswith("b"):
    print("Your name starts with 'b'!")
else:
    print("Your name not starts with a or b!")


userInput2 = input("Write somethings..: ")
if userInput2.endswith("hil"):
    print("hil!")
else:
    print("not!") #simple examples :p


# split() Function

" split(x) "

userInput3 = input("Write somethings..: ")
words = userInput3.split(" ")
print("There is {} words in your sentence!".format(len(words)))
for number, w in enumerate(words):
    print(number + 1, w)

    #another example

aboutMe = "Hello! Idk what I write here".split(" ")
print(aboutMe)

# strip(), lstrip(), rstrip()

language = "                Python                              "
print(language.strip(" "))  #"Python"
print(language.lstrip(" ")) #"Python             "
print(language.rstrip(" ")) #"           Python"


    #Another example
""" Let's say we're getting e-mails like that

>>>>>>>>>>>>>>>>>>>>>>>>> Hello.. bla bla..
>>>>>>>>>>>>>>>>>>>>>>>>> I am.. bla bla.. """


content = """>>>>>>>>>>>>>>>>>>>>>>>>> Hello.. bla bla.."""


print("Default content:\n", content)
print("Stripped content:\n", content.strip(">"))



# join() Function

listX = ["22", "2", "2019"]
print("ListX:", "/".join(listX))

listY = ["G", "O", "R", "A"]
print(".".join(listY))


# count() Function

# count(x) or count(x, index)

lyrics = """First things first
I'ma say all the words inside my head
I'm fired up and tired of the way that things have been, oh ooh
The way that things have been, oh ooh
Second thing second
Don't you tell me what you think that I can be
I'm the one at the sail, I'm the master of my sea, oh ooh
The master of my sea, oh ooh"""

print(lyrics.count("a"))
    #or

print(lyrics.count("a", 25)) #25.index included


#find and rfind()
""" If parameter is found, then return the first index of parameter
    If can't foundt, return -1"""

print(lyrics.find("words"))

print(lyrics.find("nihil")) #-1

nihil = lyrics.find("nihil")
print(2 * nihil) # -2

# rfind is searching from the end

print(lyrics.rfind("ooh"))