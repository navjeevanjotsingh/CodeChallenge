################################################################
#### Code Author: Navjeevan Jot Singh Salana ###################
#### Date: December 12 2019 ####################################
################################################################
import json
import sys
import math
import csv
from datetime import datetime
import collections

# defining argv for making sure the script takes CSV or JSON files as inputs
if len(sys.argv) < 2:
    print "Please provide the inputs in the following format \n python <script.py> <either JSON file> or <CSV file>"
    sys.exit()

#invoking the sys.argv to allow arguments at script run
path = sys.argv[1]
actual_months = {}
#defining the month list
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
month_values = []

#function to tabulate the birthdays (month-wise) and the corresponding number of people
def BirthMonthTally(birthmonth):
    #extracting the birthtimestamp from the file
    birthmonth = [str(items_birthmonth) for items_birthmonth in birthmonth]
    birthmonthlen = len(birthmonth)

    for dt in range(0, birthmonthlen - 1):
        try:
            #converting the epoch time to human readable time and fetching the month value
            epochTS = datetime.fromtimestamp(int(birthmonth[dt])).strftime('%m')
            month_values.append(epochTS)
        except:
            #Implementing the exception handling, for the "wrong" 'out-of-bound' timestamps in the dataset
            pass

    print("\nFOLLOWING MONTHS HAVE THE NUMBER OF BIRTHDAYS IN REGARDS TO THE DATASET")
    print("------------------------------------------------------------------------")
    monthlist = collections.Counter(month_values)
    actual_months = sorted(monthlist.items())
    # print(actual_months)
    # swapping the new key indicating month names
    try:
        for key, value in actual_months:
            print(month_list[int(key) - 1], value)
    except:
        pass
    print("------------------------------------------------------------------------\n")

#function to tabulate top 3 food and the corresponding number of people who like it
def FavoriteFoodTally(empty_var_favorite_food):
    foodlist = collections.Counter(empty_var_favorite_food)
    liftoffavfood = sorted(foodlist.items(), reverse=True, key=lambda x: x[1])
    print "\nTOP 3 FAVORITE FOOD ITEMS WITH THE NUMBER OF PEOPLE LIKING IT ARE:"
    print "-------------------------------------------------------------------- \n"

    countr = 0
    for food in liftoffavfood:
        countr += 1
        print (food[0], ':', food[1])
        if countr > 2:
            break


def ReadJSON():
    # loading the JSON file using path
    with open(path_json) as input_json:
        dict_json = json.load(input_json)
        empty_var_siblings = []
        empty_var_favorite_food = []
        empty_var_birthmonth = []
        for data_json in dict_json:
            siblings_val = (data_json['siblings'])
            favorite_food_val = (data_json['favourite_food'])
            birthtime_val = (data_json['birth_timestamp'])
            empty_var_siblings.append(siblings_val)  #appending siblings column fetch
            empty_var_favorite_food.append(favorite_food_val)  #appending favorite food column fetch
            empty_var_birthmonth.append(birthtime_val)  # appending birth timestamp column fetch

    empty_var_favorite_food = [str(items_ff).lower().strip() for items_ff in empty_var_favorite_food]
    ## Print food details
    FavoriteFoodTally(empty_var_favorite_food)
    ## Print birth month details
    BirthMonthTally(empty_var_birthmonth)

    empty_var_siblings= [str(items) for items in empty_var_siblings]
    empty_var_siblings = [int(s) for s in empty_var_siblings]
    sum1 = sum(empty_var_siblings)
    len1 = len(empty_var_siblings)
    print "\n \nTHE SIBLING INFORMATION IN REGARDS TO THE DATASET IS GIVEN BELOW:"
    print "---------------------------------------------------------------- \n"

    print "1. The total sum of siblings in the JSON dataset is: ", sum1
    print "2. The total number of entries in the JSON dataset is: ", len1
    print "3. The average (rounded-up) number of siblings in the JSON dataset is", math.ceil(sum1 / len1), "\n"




def ReadCSV():
    #reading the CSV file
    with open(path_csv, 'r') as input_csv:
        empty_var_siblings = []
        empty_var_favorite_food = []
        empty_var_birthmonth = []
        csv_read = csv.reader(input_csv, delimiter=',')
        for col in csv_read:
            siblings_val = (col[2])  # siblings column extract from csv
            birthtime_val = (col[5])  # birthtimestamp extract from csv
            favorite_food_val = (col[3])  # favorite food extract from csv
            empty_var_favorite_food.append(favorite_food_val)
            empty_var_siblings.append(siblings_val)
            empty_var_birthmonth.append(birthtime_val)

    # removing the header from each of the list
    list_csv_sibling = list(empty_var_siblings)
    list_csv_sibling.pop(0)
    empty_var_siblings.pop(0)
    # print empty_var_siblings   #can be uncommented to see the siblings extracted list
    list_csv_favoritefood = list(empty_var_favorite_food)
    list_csv_favoritefood.pop(0)
    empty_var_favorite_food.pop(0)
    # print empty_var_favorite_food #can be uncommented to see the favorite-food extracted lis
    list_csv_birthmonth = list(empty_var_birthmonth)
    list_csv_birthmonth.pop(0)
    empty_var_birthmonth.pop(0)
    # print list_csv_birthmonth #can be uncommented to see the birthmonth extracted lis

    siblings_unicode = [str(items1) for items1 in list_csv_sibling]
    siblings_unicode = [int(s1) for s1 in list_csv_sibling]
    sum1 = sum(siblings_unicode)
    len1 = len(siblings_unicode)
    print("\n \nTHE SIBLING INFORMATION IN REGARDS TO THE DATASET IS GIVEN BELOW:")
    print("---------------------------------------------------------------- \n")
    print("1. The total sum of siblings in the CSV dataset is: ", sum1)
    print("2. The total number of entries in the CSV dataset is: ", len1)
    print("3. The average (rounded-up) number of siblings in the CSV dataset is", math.ceil(sum1 / len1), "\n")
    FavoriteFoodTally(empty_var_favorite_food)
    BirthMonthTally(empty_var_birthmonth)


if path.endswith('.json'):
    path_json = sys.argv[1]
    ReadJSON()
elif path.endswith('.csv'):
    path_csv = sys.argv[1]
    ReadCSV()
else:
    print("Please provide the file in the specified format with the correct file extensions \n python <script.py> <either JSON file> or <CSV file>")
    exit()