##################Code exercise: Speed dating
##################We will write a mixer for two groups of people so they can get to know each other 

#Ex 1: Write a list containing seven male names, and a list containing seven female names. Call the male names group_a and the female names
# group_b

#We want these two groups of people to mix with. Write a function that randomly assigns the people into pairs by randomly picking a 
# person from group A and one from goup B and saving the result in a dictionary. Do this until all people are paired up with a person from 
# the other group!
import random

group_a = ["Sal", "Joe", "Phil"]

group_b = ["Penny", "Alice", "Susan"]

size = len(group_a)

def matching_people(group_a, group_b):
    res_dict = {}
    for i in range(0, len(group_a)):
        idx = random.randint(0, (len(group_b)-1))
        res_dict[group_a[i]] = group_b[idx]
        group_b.pop(idx)
    return res_dict

final_dict = matching_people(group_a, group_b)

print(final_dict)


########Exercise 2: Since the two people won't know each other, we can help them by telling them what they should wear so they 
# can recognize each other. Create a list of colours and create a similar dictionary as in Exercise 1, but this time the person 
# who is the key should give back a list as it's value, where the first element is the name of the person and the second element
# is the colour that person should wear. 

group_a = ["Sal", "Joe", "Phil"]

group_b = ["Penny", "Alice", "Susan"]

colours = ["Blue", "Red", "Green"]

def matching_people_with_colours(group_a, group_b, colours):
    res_dict = {}
    for i in range(0, len(group_a)):
        idx = random.randint(0, (len(group_b)-1))
        idx_02 = random.randint(0, (len(group_b)-1))
        res_dict[group_a[i]] = [group_b[idx], colours[idx_02]]
        group_b.pop(idx)
        colours.pop(idx)
    return res_dict

print(matching_people_with_colours(group_a, group_b, colours))









