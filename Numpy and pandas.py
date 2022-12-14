from asyncio.windows_events import NULL
import numpy as np
import random
import pandas as pd

random.seed(10)
#################################Introduction: Numpy and Random
# lst = [i for i in range(0,100,6)]

# print(lst)

# print(np.median(lst))

# print(np.mean(lst))

## Removing items
# ##By value: 
# lst.remove(12)

# print(lst)

# ##By index: 
# lst.pop(0)

# print(lst)

################Random 

# lst = [i for i in range(0,501)]

# random_int = random.randint(0,500)

# print("This time the random integer was: {}".format(lst[random_int]))

# print(f"This time the random integer was {lst[random_int]}")

##########Getting random elements in a list

# names_list = ["Ringo Starr", "John Lennon", "Paul McCartney", "George Harrison"]

# random_beatle = names_list[random.randint(0,3)]

# print("This week we will be talking about {} from the Beatles".format(random_beatle))


###############List sorting and List comprehensions with functions
#####Intro to functions with binary logic

# def even_uneven(number_01):
#     '''
#     This function takes in an integer, and returns whether it is even or not. 
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

# lst = [i for i in range(0,50)]

# lst_even = [i for i in range(0,50) if i % 2 == 0]

# print(lst_even)


# ####Functions applied to list comprehensions
# lst_even_multiplied = [multiplied_by_three(i) for i in range(0,50) if i%2 == 0]

# print(lst_even_multiplied)


############################Lesson 1: Create a pandas dataframe from lists:

# lst_names = [['tom', 25], ['krish', 30],
#        ['nick', 26], ['juli', 22]]
    
# df = pd.DataFrame(lst_names, columns =['Name', 'Age'])

# print(df)

############################Lesson 2: Sub-setting Columns and Rows
#Explicit referencing:

#loc selects rows and columns with specific labels
#iloc selects rows and columns at specific integer positions

###############Example df.loc:
#df.loc[rows, columns]
#print(df.loc[:,"Name"])

###############Example df.iloc
#df.iloc[rows, columns]
#print(df.iloc[:, 0])

############################Lesson 3: Getting averages from rows and columns 
#print(np.mean(df.loc[:, "Age"]))

###########################Lesson 4: Creating DataFrmes from dictionaries:

# data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
# df_dict = pd.DataFrame.from_dict(data)
# print(df_dict)

###########################LEsson 5: Sample Dataframes
# mead_dataframe = pd.read_excel("C:\\Users\\davim\\Desktop\\The Montani Mead Makery.xlsx")

# print(mead_dataframe)

# print(mead_dataframe.columns)

# print(mead_dataframe["Initial gravity"])

#print(np.mean(mead_dataframe["Initial gravity"]))

###############Removing unwanted rows 


# #########First intuition
# for i in mead_dataframe["Initial gravity"]:
#     print(i)
#     print(type(i))

##########The proper way
# kill_list = []

# for i in range(0, len(mead_dataframe["Initial gravity"])):
#     print(i)
#     print(mead_dataframe["Initial gravity"][i])
#     if type(mead_dataframe["Initial gravity"][i]) is str:
#         print("This is a string")
#         kill_list.append(i)
#         mead_dataframe = mead_dataframe.drop(i)


# print(kill_list)
# print(mead_dataframe["Initial gravity"])
# print("The mean of the starting Gravities is {}".format(np.mean(mead_dataframe["Initial gravity"])))

################Clean sample Dataframe
# salsa_canteen = pd.read_excel("C:\\Users\\davim\\Desktop\\Institut am Rosenberg\\Dave's Salsa Canteen.xlsx")

# print(salsa_canteen)


##############################Cleaning dataframes, and indexing###################################

###Checking for Null values:
# data = {'col_1': [3, 2, None, 0], 'col_2': ['a', 'b', 'c', 'd']}
# df_dict = pd.DataFrame.from_dict(data)
# print(df_dict)

# print(df_dict.isnull().values.any())

# ##Also drop all the na values
# df_dict = df_dict.dropna()
# print("After dropping the NA values")
# print(df_dict)

# #Drop specific values in a specific column using subsets:
# print("After dropping a specific value")
# df_dict = df_dict[df_dict.col_2 != "a"]

# print(df_dict)

# #Checking all cells with a For-Loop: Warning! Last resort! 
# print("After the for-loop")

# df_dict = df_dict.reset_index(drop= True)

# for j in range(0,df_dict.shape[0]):
#     for i in range(0,df_dict.shape[1]):
#         if df_dict.iloc[i, j] == 'd':
#             pass
#             #df_dict.iat[i,j] = None
#             #df_dict = df_dict.drop([j])
#         else:
#             pass

# print(df_dict)

# from Mini_mart_desgin import salsa_canteen_dct
# ####Descriptive Statistics:
# #Create a new column based on other columns: 
from Mini_mart_desgin import salsa_canteen_dct

print(salsa_canteen_dct.columns)

salsa_canteen_dct["Total_Earnings"] = salsa_canteen_dct['Quantity'] * salsa_canteen_dct["Price"]

print(salsa_canteen_dct.columns)

print(salsa_canteen_dct["Total_Earnings"].mean())

print(salsa_canteen_dct["Total_Earnings"].min())

print(salsa_canteen_dct["Total_Earnings"].max())

# Total_Earnings_Per_Customer = salsa_canteen_dct.groupby('Customer').sum(['Total_Earnings'])

# print(Total_Earnings_Per_Customer)
# best_value = max(Total_Earnings_Per_Customer['Total_Earnings'])

# name = Total_Earnings_Per_Customer.loc[Total_Earnings_Per_Customer['Total_Earnings'] == best_value]

# print('Your best customer has: {} earnings and is {}'.format(best_value, name.index[0]))