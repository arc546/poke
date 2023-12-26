import random
from pokemonclass import *
    

def main():
    pokenum = random.choice(list(range(1,1009))) #All pokemon from gen 1 to vanilla gen 9
    pokechoice = Pokemon(pokenum)
    text, gameVers = pokechoice.getRndmDexEntry()
    text = textClean(pokechoice, text)
    guessingGame(pokechoice, text, gameVers)
    
def textClean(pokemon, text):
    if pokemon.name().upper() in text:
        text = text.replace(pokemon.name().upper(),"REDACTED")
    elif pokemon.name() in text:
        text = text.replace(pokemon.name(),"REDACTED")
    return text

def guessingGame(pokemon, text, gamevers):
    s = f"The Pokemon I'm thinking of is #{str(pokemon.getNatDexNum())} and has type(s) {' '.join([i for i in pokemon.getType()])} You have three tries, goodLuck"
    count = 0
    print(s)
    while count < 3:
        if count == 2:
            print(f"Looks like you need a little bit of help... I'll give you a dex entry of the pokemon:\n")
            print(f"{text} from Pokemon {gamevers}\n")
            print("Hopefully that helps")
        guess = input(f"guess #{count+1} is? ")
        if guess == pokemon.name():
            print("You Win!")
            return
        else:
            count += 1
    print("\n",pokemon,"\n")
    print("Looks like you lose! better luck next time!")
        


if __name__ == "__main__":
    main()
    

