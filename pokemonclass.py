import requests
import random

class Pokemon():
    
    def __init__(self, pokeID="1"):
        self.__ID = pokeID
        self.__pokeAPIData = (requests.get("https://pokeapi.co/api/v2/pokemon/" + str(self.__ID))).json()
        self.__speciesAPIData = (requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(self.__ID))).json()
        self.__types = self.gettype(giveback = False)
        self.__dexEntries = self.__createdexlib()
        self.__name = self.getname(giveback = False)
    
    def __str__(self):
        s = f"The pokemon is #{self.__ID} in the National Dex and is named {self.__name}, with the type(s) {' '.join(i for i in self.__types)}"
        return s
    
    def __repr__(self):
        s = "id <" + str(id(self)) + "> "
        return s
    
    def getname(self, giveback=True):
        if giveback == True:
            return self.__name
        else:
            return self.__pokeAPIData["species"]["name"].capitalize()
        

    def gettype(self, giveback=True):
        if giveback == True:
            return self.__types
        else:
            type = self.__pokeAPIData["types"]
            pokeTypes = []
            for _, j in enumerate(type): 
                pokeTypes.append(j["type"]["name"].capitalize())
            return pokeTypes
    
    def __createdexlib(self):
        flavText = self.__speciesAPIData["flavor_text_entries"]
        dexes = []
        for i in range(len(flavText)):
            if flavText[i]["language"]["name"] == "en":
                dexes.append(flavText[i])
        return dexes
    
    def getrndmdexentry(self):
        dex = self.__dexEntries
        rndmNum = random.randint(0,len(dex)-1)
        text = dex[rndmNum]["flavor_text"].replace("\n", " ")
        text = text.replace("\x0c", " ")
        text = text.replace("\x0b", " ")
        gameVers = dex[rndmNum]['version']['name'].capitalize()
        return text, gameVers
    
    def getnatdexnum(self):
        return self.__ID