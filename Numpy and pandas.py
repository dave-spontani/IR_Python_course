import numpy as np
import random
import pandas as pd

#################################Introduction: Numpy and Random
# lst = [i for i in range(0,100,6)]

# print(np.median(lst))

# print(np.mean(lst))

##Get the length of a list

## Removing items
##By value: 
# lst.remove(0)

##By index: 
# lst.pop(0)


################Random 

# lst = [i for i in range(0,500)]

# random_int = random.randint(0,500)

# print("This time the random integer was: {}".format(lst[random_int]))

##########Getting random elements in a list

# names_list = ["Ringo Starr", "John Lennon", "Paul McCartney", "George Harrison"]

# random_beatle = names_list[random.randint(0,3)]

# print("This week we will be talking about {} from the Beatles".format(random_beatle))


###############List sorting and List comprehensions with functions
#####Intro to functions with binary logic

# def even_uneven(number_01):
#     '''
#     This function takes in an integer, and returns whether it is even or not. If a float is inputted, the 
#     function will tell the user to input an integer
#     '''
#     if number_01 % 2 == 0:
#         print("This number is even")
#         return True

#     else :
#         print("This integer is odd")
#         return False


# even_uneven(2)
    
# def multiplied_by_three(x):
#     return x * 3

#####List comprehensions (repetition)

#lst = [i for i in range(0,50)]

#lst_even = [i for i in range(0,50) if i % 2 == 0]

# print(lst_even)


####Functions applied to list comprehensions
#lst_even_multiplied = [multiplied_by_three(i) for i in range(0,50) if i%2 == 0]

# print(lst_even_multiplied)


############################Lesson 1: Create a pandas dataframe

# lst_names = [['tom', 25], ['krish', 30],
#        ['nick', 26], ['juli', 22]]
    
# df = pd.DataFrame(lst_names, columns =['Name', 'Age'])

# print(df)

############################Lesson 2: Sub-setting Columns and Rows
#Explicit referencing

#loc and iloc

############################Lesson 3: Getting averages from rows and columns 
# print(np.mean(df["Age"]))

###########################LEsson 4: Sample Dataframes
# mead_dataframe = pd.read_excel("C:\\Users\\davim\\Desktop\\The Montani Mead Makery.xlsx")

# print(mead_dataframe)

# print(mead_dataframe.columns)

# print(mead_dataframe["Initial gravity"])


#print(np.mean(mead_dataframe["Initial gravity"]))

###############Removing unwanted rows 
# kill_list = []

#########First intuition
# for i in mead_dataframe["Initial gravity"]:
#     print(i)
#     print(type(i))

##########The proper way
# for i in range(0, len(mead_dataframe["Initial gravity"])):
#     print(i)
#     print(mead_dataframe["Initial gravity"][i])
#     if type(mead_dataframe["Initial gravity"][i]) is str:
#         print("This is a string")
#         kill_list.append(i)
#         # mead_dataframe = mead_dataframe.drop(i)


# print(kill_list)
# print(mead_dataframe["Initial gravity"])
# print("The mean of the starting Gravities is {}".format(np.mean(mead_dataframe["Initial gravity"])))

################Clean sample Dataframe
# salsa_canteen = pd.read_excel("C:\\Users\\davim\\Desktop\\Institut am Rosenberg\\Dave's Salsa Canteen.xlsx")

# print(salsa_canteen)
