import requests
import random

class Pokemon():
    
    def __init__(self, pokeID="1"):
        self.__pokeAPIData = (requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokeID).lower())).json()
        self.__speciesAPIData = (requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(pokeID).lower())).json()
        self.__ID = self.getNatDexNum(giveback = False)
        self.__types = self.getType(giveback = False)
        self.__dexEntries = self.__createdexlib()
        self.__name = self.name(giveback = False)
        self.__abilities, self.__hiddenabilities = self.getAbilities()
    
    def __str__(self):
        if len(self.__abilities) > 1:
            abilitiesS = f"{', '.join(map(str,self.__abilities[:len(self.__abilities)-1]))}, and {self.__abilities[-1]}"
        else:
            abilitiesS= f"{''.join(map(str,self.__abilities))}"
        s = f"The pokemon is #{self.__ID} in the National Dex and is named {self.__name}, with the type(s) {', '.join(map(str,self.__types))}. \nIt has the potential abilitie(s) {abilitiesS}"
        return s
    
    def __repr__(self):
        s = "id <" + str(id(self)) + "> "
        return s
    
    def name(self, giveback=True):
        if giveback == True:
            s = self.__name
        else:
            s = self.__pokeAPIData["species"]["name"].capitalize()
        return s 
        

    def getType(self, giveback=True):
        if giveback == True:
            pokeTypes = self.__types.copy()
        else:
            type = self.__pokeAPIData["types"]
            pokeTypes = []
            for _, j in enumerate(type): 
                pokeTypes.append(j["type"]["name"].capitalize())
        return pokeTypes
    
    def __createdexlib(self, ):
        flavText = self.__speciesAPIData["flavor_text_entries"]
        dexes = []
        for i in range(len(flavText)):
            if flavText[i]["language"]["name"] == "en":
                dexes.append(flavText[i])
        return dexes
    
    def getRndmDexEntry(self):
        dex = self.__dexEntries
        rndmNum = random.randint(0,len(dex)-1)
        text = dex[rndmNum]["flavor_text"].replace("\n", " ")
        text = text.replace("\x0c", " ")
        text = text.replace("\x0b", " ")
        gameVers = dex[rndmNum]['version']['name'].capitalize()
        return text, gameVers
    
    def getDexEntry(self, vers):
        dex = self.__dexEntries
        text = "Error, No Dex Entry for this specific pokemon in that version..."
        for i in dex:
            if i["version"]["name"] == vers.strip().lower():
                text = i["flavor_text"].replace("\n", " ")
                text = text.replace("\x0c", " ")
                text = text.replace("\x0b", " ")
        return text
    
    def getNatDexNum(self, giveback=True):
        if giveback == True:
            output = self.__ID
        else:
            output = self.__pokeAPIData["id"]
        return output

    def getAbilities(self):
        abilities = []
        hiddenAbilities = []
        for i in self.__pokeAPIData["abilities"]:
            if i["is_hidden"] == True:
                hiddenAbilities.append(i["ability"]["name"])
            abilities.append(i["ability"]["name"])
        return abilities, hiddenAbilities
    
    def captureRate(self):
        n = self.__speciesAPIData["capture_rate"]
        return n
    
    def height(self):
        height = self.__pokeAPIData["height"]
        return height
    
    def weight(self):
        weight = self.__pokeAPIData["weight"]
        return weight
    
