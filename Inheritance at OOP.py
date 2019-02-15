# INHERITANCE AT OBJECT ORIENTED PROGRAMMING!

class Games():

    def __init__(self, gameName, gameType):
        print("""
        
        
#### Do not forget: init always works first! #### 
         
         
        """)
        self.gameName = gameName
        self.gameType = gameType

    def showGameInfos(self):
        print("""
        ### ALL ABOUT GAME ###
        Game name: {}
        Game type: {}
        """.format(self.gameName, self.gameType))


class Companies(Games):

    def __init__(self, gameName, gameType, gameCompany):
        super().__init__(gameName, gameType)
        self.gameCompany = gameCompany

    def showCompanyInfos(self):
        print("""
        ### ALL ABOUT GAME COMPANY ###
        Company name:   {}
        Game names:     {}
        Game types:     {}
        """.format(self.gameCompany, self.gameName, self.gameType))

blizzard = Companies("World Of Warcraft", "MMO", "Blizzard")
blizzard.showCompanyInfos()


"""
WHAT WE DID HERE?

1) We get everything from first Class (Games)
2) We created __init__ again and added gameCompany (Override)
3) Used super() Function
   Why? Because we don’t wanna create old parameters again and again.
4) And Show Infos Overrided.
"""