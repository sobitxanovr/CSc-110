###
### Author: Rustambek Sobithanov
### Class: CSc 110
### Description: The following lines of code ask a user for eight inputs (names of people,
###               a pet, place etc.) and by using them, make up a story
###
male_name = input('A male name:\n')
female_name = input('A female name:\n')
pet_name = input('A pet name:\n')
place = input('A place:\n')
adjective = input('An adjective:\n')
animal = input('An animal:\n')
verb_ing = input('A verb ending in ing:\n')
adverb = input('An adverb:\n')
print('----------')
print(male_name + """ and """ + female_name + """ were best friends.
One day """ + male_name + """ and """ + female_name + """ decided to go on a
vacation to """ + place + """. However, they didn't know
what to do with their """ + adjective + """ pet """ + animal + """ named """ + pet_name + """.
""" + pet_name + """ had been causing problems, due to constant """ + verb_ing + """.
""" + male_name + """ found a sitter for their pet, and """ + adverb + """ went on the trip.""")