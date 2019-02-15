# OBJECT ORIENTED PROGRAMMING!

class peoples():
    mostOfThem = "STUPID"
    littlePartOfThem = "Special Ones!"

""" Now we can create object with using that class """

neighbor = peoples.mostOfThem
print(neighbor)

Viz = peoples.littlePartOfThem
print(Viz)

print(type(Viz)) # <class 'str'>

""" Here is a problem that we can create objects but we can't change the values! """

# __init__() Function!

""" Do not forget: init always works first! """

class Games():

    def __init__(self, gameName, gameType):
        print("""
        
        
#### Do not forget: init always works first! #### 
         
         
        """)
        self.gameName = gameName
        self.gameType = gameType

""" Now we can create object as what we want! """

wOw = Games(gameName = "World Of Warcraft", gameType = "MMO")
print("What is the game name?", wOw.gameName, sep = "\n")
print("What is the type of", wOw.gameName + "?\n", wOw.gameType, sep = "")