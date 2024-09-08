

# Author: Carl Mesias
# Link: https://www.youtube.com/watch?v=kqtD5dpn9C8



###################################################################
###################################################################
##--------------------------- Variables -------------------------##

new_integer     = 10
new_string      = "I'm a string!"
new_boolean     = True
new_list        = ["Herald", "Athen", "Aether", "Eon"]

print("Integer: ", new_integer)
print("String:  ", new_string)
print("Boolean: ", new_boolean)
print("List:    ", new_list)
print("")

###################################################################
###################################################################
##---------------------------- Strings --------------------------##

# create course string name
course = "Python for Beginners"

# capitalize course name then print
print(course.upper())

# find index of y
print("Index of y is '" + str(course.find("y")) + "'")

# replace 'Beginners' with 'Intermediates'
print(course.replace("Beginners", "Intermediates"))
print("")

###################################################################
###################################################################
##--------------------- Arithmetic Operators --------------------##

a_num = 0
a_num += 19
print(str(a_num))       # 19

print(5 + 3)            # 8, add
print(5 - 3)            # 2, subtract
print(5 * 3)            # 15, multiply
print(10 / 3)           # 3.3333333333333335, returns a float
print(10 // 3)          # 3, returns integer
print(10 % 3)           # 1, remainder is 1
print(5 ** 2)           # 25, 5 to the power of 2
print("")

###################################################################
###################################################################
##--------------------- Comparison Operators --------------------##

cloud_winning_number    = 457284
user_lottery_number     = 356284

if cloud_winning_number == user_lottery_number:
    print("Congrats you match the winning number!")
else:
    print("Sorry you lose the lottery!")

###################################################################
###################################################################
##----------------------- Logical Operators ---------------------##

price = 25

print(20 < price < 30)   # True, print(price > 20 and price < 30)
print("")

###################################################################
###################################################################
##------------------------- If Statements -----------------------##

temperature = 27

if temperature > 30:
    print("It's hot today!")
elif temperature > 20:
    print("It's a cool day!")
else:
    print("It's a cold day!")

print("")

###################################################################
###################################################################
##------------------------- While Loops -------------------------##

startIdx = 0
print("Start index: " + str(startIdx))

while startIdx < 10:
    startIdx += 1
    print("startIdx: " + str(startIdx))

print("Final index: " + str(startIdx))

print("")

###################################################################
###################################################################
##---------------------------- Lists ----------------------------##

# create list of names
names = ["John", "Bob", "Sarah", "Mosh", "Sam", "Alex"]

# print all names
print("Print all names: \n", names)

# replace the first index value ('John' -> 'Donkey Kong'
print("")
print("replacing 'John' -> 'Donkey Kong'...")
names[0] = "Donkey Kong"

# replace the last index value ('Alex' -> 'Kirby')
print("replacing 'Alex' -> 'Kirby'...")
names[-1] = "Kirby"

# print all names
print("")
print("Print new names: \n", names)

# print first 3 of new names ["John", "Bob", "Sarah", "Mosh", "Sam", "Alex"]
print("")
print("Print first three of new names: \n", names[0:3])     # inclusive
print("")

###################################################################
###################################################################
##------------------------- List Methods ------------------------##

num_list = [92674, 3, 4, 533, 6]

# add 74 to the end of 'num_list'
num_list.append(74)

# insert a new number in the second index (4) with 878787
num_list.insert(2, 878787)

# remove 533
num_list.remove(533)

# print 'num_list'
print(num_list)

# check if value '92674' exists
print(92674 in num_list)

# print number of elements in the list (6)
print(len(num_list))

# clear list
num_list.clear()

# print 'num_list'
print(num_list)
print("")

###################################################################
###################################################################
##--------------------------- For loops -------------------------##

print("Temperature data: ")
temperature_data = [35, 32, 20, 24, 33]

# print each element from list
for temp in temperature_data:
    print(temp)

print("")

###################################################################
###################################################################
##---------------------- The range() function -------------------##

### Example 1 ###

# don't create, but just print 'range(0, 5)'
print(range(5))                            # range(0,5)

# use for loop to go over range of numbers
for num in range(5) :
    print(num)

print("")

### Example 2 ###

# create a range object from 5 to 10
range_numbers_10 = range(5, 10)           # exclusive
print(range_numbers_10)

# loop of range
for num in range_numbers_10:
    print(num)

print("")

### Example 3 ###
range_three_param = range (5, 10, 2)     ### 5, 7, 9
print(range_three_param)
for num in range_three_param:
    print(num)

print("")

###################################################################
###################################################################
##----------------------------- tuples --------------------------##

tuple_numbers = (5, 4, 33, 55, 68)

# replace the first index (5) with 73
# tuple_numbers[0] = 73                     # error because tuples are not immutable, you cannot modify them

###################################################################
###################################################################
##----------------------------- Classes -------------------------##

# Create a new class of residents
class Resident:
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, status, cpr, diagnosis):
        self._first_name    = first_name
        self._last_name     = last_name
        self._birth_year    = birth_year
        self._birth_month   = birth_month
        self._birth_day     = birth_day
        self._status        = status
        self._cpr           = cpr
        self._diagnosis     = diagnosis

    def __str__(self):
        return f"{self._first_name} {self._last_name} \n- Diagnosis: {self._diagnosis}"

# create a new resident named 'Jane Done', who was born on March 3, 1980, status of 'current_resident' and 'CPR' status
resident1 = Resident("Jane", "Doe",
                    1980, 3, 25,
                    "current_resident", "CPR", "High blood pressure")

# create a new resident named 'Julius Caesar', who was born on July 12, 100 BC, status of 'nonresident'  and 'DNR' status
resident2 = Resident("Julius", "Caesar",
                    100, 7, 12,
                    "current_resident", "DNR", "Very afraid of knives")

# Print Jane Doe's data
print(resident1)
print("")

# Print Julius Caesar's data
print(resident2)

### Output ###
#
#
# Jane Doe
# - Diagnosis: High blood pressure
#
# Julius Caesar
# - Diagnosis: Very afraid of knives
#
#


