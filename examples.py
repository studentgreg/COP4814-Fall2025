import main_functions

class Elf:
    def __init__(self,level,ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

# A) Create an instance of Elf named Elora
elora = Elf(1,{
            "str":13, "dex":14, "con":12,
            "int":18, "wis":16, "cha": 15
        })
print(elora)

# B) Create an instance of Elf named Elrond
elrond = Elf(2)
print(elrond)

# C) Print the value of hp for Elora
print(elora.hp)

# D) Print the value of hp for Elrond
print(elrond.hp)

# E) Print the value of level for Elora
print(elora.level)

# F) Print the value of ability_scores for Elrond
print(elrond.ability_scores)

# G) Convert the elora object instantiated above into a Python dictionary
eloraDict = elora.__dict__

# H) Printing its type:
print(eloraDict)
print(type(eloraDict))

# I) Converting elrond object instantiated above into a Python dictionary
elrondDict = elrond.__dict__

# J) Printing its type:
print(elrondDict)
print(type(elrondDict))

# K) Printing both Elrond and Elora dictionaries

# L) Serializing both Elrond and Elora dictionaries to JSON
# we need to use the function save_to_file to create the JSON file
main_functions.save_to_file(eloraDict,"elora.json")
main_functions.save_to_file(elrondDict,"elrond.json")

# M) Deserializing both Elrond and Elora JSON files to Python dictionary
data1 = main_functions.read_from_file("elora.json")
data2 = main_functions.read_from_file("elrond.json")

# N) Printing their types
print(type(data1))
print(type(data2))