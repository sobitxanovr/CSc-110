###
### Author: Rustambek Sobithanov
### Class: CSc 110
### Description: The following lines of code ask a user for six inputs (names of people,
###               a street, object etc.) and by using them, make up a story
###
female_name = input('A female name:\n')
street_name = input('A street name:\n')
male_name = input('A male name:\n')
an_object = input('An object:\n')
vehicle = input('A vehicle:\n')
adjective = input('An adjective:\n')
print('----------')
print(female_name + """ decided to move from her apartment on 5th
to a condo on """ + street_name + """. She called her friend """ + male_name + """
for help. However, they could not fit """ + an_object + """ into
the moving truck, so they had to rent a """ + adjective, vehicle + """
in order to move it!""")