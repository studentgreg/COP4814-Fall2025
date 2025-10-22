import main_functions

#Exercise 1: Using the function 'read_from_file',
# read superCompHeroes.json as a dictionary in Python,
# and print its type to confirm:
data = main_functions.read_from_file("superCompHeroes.json")
print(type(data))

#Exercise 2: Print the number of keys in superCompHeroes
print(len(data.keys()))

#Exercise 3: Print all the keys in superCompHeroes
print(data.keys())

#Exercise 4: Print the type of the value of 'members'
print(type(data["members"]))

#Exericse 5: Print its first element:
print(data["members"][0])


#Exercise 6: Print the name of the first element
print(data["members"][0]["name"])
#Notice that the structure of the data is: dict->list->dict->string

#Exercise 7: Print the strength of the second member:
print(data["members"][1]["strength"])
#Notice that the structure of the data is: dict->list->dict->int

#Exercise 8: Print the names and strengths of the Super Component Heroes
# Hint: use a for loop for the list!

for i in data["members"]:
    print(i["name"], i["strength"])

#Exercise 9: To print members in order of strength:

#Exercise 10: Create a new Super Component Hero and using the function
# 'save_to_file', overwrite the existing 'superCompHeroes.json' with
# this new entry
# IMPORTANT: automatically typing into the JSON file is not accepted
