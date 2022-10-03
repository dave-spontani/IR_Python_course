###################### A way to solve the mini-mart exercise, once with lists of lists and once with dictionaries#################
#####################Code exercise: Mini-Mart/Mini Shop
###We will create a pandas dataframe which contains the sales data of your own little Shop
###You are free to build it however you please! However, the data must be random, and you will have to meet the following requirements:
#0. All figures must be plausible
#1. A minimum of 5 columns is required: Of these 5, one column must contain the date of the sale;
#   and another column must contain the purchaser/customer (of which you are to have at the least 10 different customers). Finally, 
#   one column must contain a unique identifyer 
#2. A minimum of 10'000 entries/rows is required

#To ensure that the random results can be replicated, run the following command at the beginning of the file:
#"random.seed(10)"


#####Example 1: Dictionaries
#I will create a dataframe with 15'000 entries, and five columns. First, we will have to design the "date" column to show the date of
#the sale. For this, we will use the datetime package. I found that we can use numbers to represent dates, so I will write a function that 
#randomly increases the date by 1 or not ---> That way, we can bunch orders to one day! 
from datetime import datetime
from enum import unique
import random
from tracemalloc import start 
import itertools
import pandas as pd
random.seed(10)
#Now we build the function that allows us to bunch days together: 
def maybenewday(start_day, amount_of_times):
    date_list = []
    for i in range(0, amount_of_times):
        if random.randint(0,20) <= 2: #Here, a 10% chance (1 in 10 options) was chosen
            date_list.append(datetime.fromordinal(start_day + 1).strftime("%d/%m/%y"))
            start_day += 1 
        else: 
            date_list.append(datetime.fromordinal(start_day).strftime("%d/%m/%y"))
    return date_list

date_list = maybenewday(738028, 15000)

##Can we do this with a list comprehension? 
##Yes!
# counter = itertools.count(738028)
# new_day_list = [next(counter) if random.randint(0,20) <= 10 else (next(counter) - 1) for x in range(0,15000)]
# print(new_day_list)

#Next, we will create a list of lists with customers:
customer_og = ["Hof_Castelberg", "USMEX", "El_Taquito", "Picante", "Caliente", "Nacho's", "Burrito_King", "El_Pasador", "Azteca", "Antigua"]
        
customers_list = [customer_og[random.randint(0,9)] for i in range(0,15000)]

#Now, we will create the Unique_ID: We will smash together the first three letters of the customer, add the date, then add five random 
# numbers. 

unique_id = [customers_list[i][0:3] + str(date_list[i]) + str(random.randint(0,100)) + str(random.randint(0,100)) + str(random.randint(0,100)) for i in range(0,15000)]

#The price/product catalogue
prod_og = ["Verde", "Frankensalsa", "Picante", "Roja"]

price_to_prod = [15,12,20,10]
#MAkign the dictionary that then allows us to access the proper price for each product
prod_dct = {k:v for (k,v) in zip(prod_og, price_to_prod)} 

prod_list = [prod_og[random.randint(0,3)] for i in range(0,15000)]
#Sales
sales_list = [random.randint(1,80) for i in range(0,15000)]

price_list = [prod_dct[prod_list[i]] for i in range(0,15000)]

###Creating the final DF with a dictionary: 

# final_dct = {"Date": date_list, "Customer": customers_list, "UID": unique_id, "Product":prod_list, "Quantity":sales_list, "Price":price_list}

# salsa_canteen_dct = pd.DataFrame.from_dict(final_dct)

# print(salsa_canteen_dct.head(20))

# ####Creating one from a list of lists: 
# double_list = [[date_list[i], customers_list[i],unique_id[i], prod_list[i], sales_list[i], price_list[i]] for i in range(0,15000)]

# salsa_canteen_list = pd.DataFrame(double_list, columns=["Date", "Customer", "UID", "Product", "Quantity", "Price"])

# print("And here the second last bit!")
# print("")
# print(salsa_canteen_list.head(20))


###The mother of all list comprehensions

allinone = [[date_list[i], [customer_og[random.randint(0,9)] for i in range(0,15000)][i],[customers_list[i][0:3] + str(date_list[i]) + str(random.randint(0,100)) + str(random.randint(0,100)) + str(random.randint(0,100)) for i in range(0,15000)][i], [prod_og[random.randint(0,3)] for i in range(0,15000)][i], [random.randint(1,80) for i in range(0,15000)][i], [prod_dct[prod_list[i]] for i in range(0,15000)][i]] for i in range(0,15000)]
print("And here the last bit!")
print("")
salsa_canteen_allinone = pd.DataFrame(allinone, columns=["Date", "Customer", "UID", "Product", "Quantity", "Price"])

print(salsa_canteen_allinone.head(20))


