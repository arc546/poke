In this Repo are two files, poke.py and pokemonclass.py


The file pokemonclass.py contains a so called "mini-wrapper" of PokeAPI by Paul Hallett that fetches pokemon info about basics about pokemon species, such as their type, various dex entries and the specific name of the pokemon. It does this through the use of a class
defined as Pokemon:
to create an object of this class simply call the Pokemon class with a national dex ID. as demonstrated below:

a = Pokemon(4)

this will create an object of the Pokemon class, more specifically, a is now designated as the Pokemon with a national dex ID of 4, AKA. it is the pokemon Charmander.
you can confirm this by printing out the object which output the national dex number, the name of the pokemon and it's types in an easily readable string
some other methods of the class you may find useful are gettype() which returns a list of all the types of the pokemon. getname() which returns the name of the pokemon
getnatdexnum() which returns the national dex number, and getrndmdexentry() which returns a random flavor text entry of the pokedex from one of the game versions the pokemon appears in.
Currently this is all the methods that are included in this class as I did not make it with the intent to be widespread but to be used mainly for the contents of poke.py. However, I will be working on updating it to
cover anything you would want about the pokemon specifically (eg. abilities, height, catch rate etc.) in the near future. Also note dex entries do not work for pokemon added after the vanilla releases of Scarlet and Violet (Walking Wake and onwards)
this is because the PokeAPI currently does not contain the flavor text of these pokemon for some reason...

poke.py contained the main project that this stemmed from, which was a pokemon-guessing game where the program would pick a random pokemon and give the user the national dex number and it's types and the user would have to guess which pokemon it is.
Currently, it has no GUI and only exists as a program utilizing user-input. You can play around with it if you wish, it may or may not be updated later.
