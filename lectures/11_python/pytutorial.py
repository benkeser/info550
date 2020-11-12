import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


######### Some Basic Commands #########

print('Hello World!')

print(3 + 3)


############# Data Types ##############

print(type(3))

print(type(3.0))

print(type('hello'))

print(type(True))

print(type(3 == 3))



########### Data Structures ###########

# Lists ##
foo = [1, 2, 3]

bar = ['a', 'b', 'c']

baz = [16, 'apple', 17.4, True]

print(foo, bar, baz)

print(type(foo))

print(foo[0])

print(baz[:])

## Sets ##

new_set = {1, 2, 1, 2, 3, 4, 1}

print(new_set)

foo_set = set(foo)

print(foo_set)

print(foo_set[0])

# MINI BREAKOUT: Find out why the line directly above doesn't work.

# Question: How can we get the unique elements of a list? #


# Dictionaries ##

state_dict = {'Pennsylvania' : 20,
              'Arizona' : 11,
		      'Georgia' : 16,
		      'Nevada' : 6,
		      'Michigan' : 16,
		      'Wisconsin' : 10}

print('Georgia has', state_dict['Georgia'], 'Electoral Votes')

print(state_dict.keys())

print(state_dict.values())


############# Conditionals ############

num1 = 5
num2 = 100

if num1 > num2:
	print(num1, 'is greater than', num2)

elif num1 < num2:
	print(num1, 'is less than', num2)

else:
	print(num1, 'is equal to', num2)



############## For Loops ##############

#iterate over a range
#This says 'do some task 10 times'
for i in range(10):
	print(i)

#iterate over a different range
#In range(u,l), u is inclusive, l is not
for i in range(1,5):
	print(i)

#iterate over items in a list
foo = ['a', 'b', 'c', 'd']

for letter in foo:
	print(letter)

#a list is one of many data structures that is iterable
#Standard programming practice: 
#DON'T modify a data structure as you iterate over it


# MINI BREAKOUT: How can I iterate over a dictionary's
#keys? What about its values? Can I iterate over both
#at the same time?

#Next let's add some extra states to the dictionary
#and give them some regions.
state_dict = {'Pennsylvania' : [20, 'Midwest'],
              'Arizona' : [11, 'Southest'],
		      'Georgia' : [16, 'South'],
		      'Nevada' : [6, 'West'],
		      'Michigan' : [16, 'Midwest'],
		      'Wisconsin' : [10, 'Midwest'],
		      'Florida' : [29, 'South'],
		      'Texas' : [38, 'Southwest'],
		      'Louisiana' : [8, 'South'],
		      'New Mexico': [5, 'Southwest']}


for key,val in state_dict.items():
	if val[0] > 10 and val[1] == 'South':
		print(key, 'is a key southern state.')


# #How could I quickly modify the code above to include Southwestern states?
# #I can think of 2 ways...




############# While Loops #############

#When to use a while loop?
#Keep iterating until a condition is met.
#Let's use a while loop to compute a factorial
num = 5
fac = 1
while num > 1:
	fac = fac*num
	num = num - 1

print(5, 'factorial is', fac)

#We can shorten the x = x - y notation with:
# +=
# -=
# *=


# Two useful key words: break and continue
# Use break in a loop to specify a condition to end the loop early
# Use continue to specify a condition to move on to the next iteration

state_dict = {'Pennsylvania' : [20, 'Midwest'],
              'Arizona' : [11, 'Southest'],
		      'Georgia' : [16, 'South'],
		      'Nevada' : [6, 'West'],
		      'Michigan' : [16, 'Midwest'],
		      'Florida' : [29, 'South'],
		      'Wisconsin' : [10, 'Midwest'],
		      'Texas' : [38, 'Southwest'],
		      'Louisiana' : [8, 'South'],
		      'New Mexico': [5, 'Southwest']}

count = 0
states_won = []
for state, info in state_dict.items():
	count += info[0]
	states_won.append(state)

	if count >= 270:
		print('We have a winner with states:')
		print(', '.join(states_won))
		break

	elif 'Pennsylvania' in states_won and 'Michigan' in states_won and 'Wisconsin' in states_won:
		print('We almost certainly have a winner with states:')
		print(', '.join(states_won))
		break

#How might we use continue? What if we have a lot of computationally expensive
#steps in each iteration but know we can skip an iteration under certain circumstances?

############## Functions ##############

def sum_fun(a, b):
	'''
	This function takes two input numbers
	and returns their sum

	Input: a (int/float), b(int/float)
	Output: my_sum(int/float)
	'''
	my_sum = a + b

	return(my_sum)

print(sum_fun(5, 7))

#### Functions as Input and Output ####

#let's define 4 functions
def add(num1, num2):
	return(num1 + num2)

def subtract(num1, num2):
	return(num1 - num2)

def multiply(num1, num2):
	return(num1, num2)

def divide(num1, num2):
	if num2 != 0:
		return(num1/num2)
	else:
		print('No division by 0!')

#now one more function that takes one
#of the above as its last argument
def do_math(num1, num2, operation):
	return(operation(num1, num2))

print(do_math(5, 10, add))

#Here's another example:
#filter() is a function that takes a list and a function as args
#filter() returns an iterable containing elements that, when
#passed to the given function, result in True

#Here's a list:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Let's use filter to return just even numbers

evens = list((filter(lambda x: x%2 == 0, my_list)))
print(evens)



#What if we want to return a function?
#We can again use lambdas


def add(n):
    return lambda a : a + n

add_100 = add(100)

print(type(add_100))

print(add_100(5))


#This feature actually exists in R as well
#and comes in handy when using the apply() family of functions


######### List Comprehensions #########

#Faster than for loops!
#Look through a list and return certain values into a new list

#Get rid of this sort of code:
foo = []
bar = [1, 17, 8, 83, 26, 11, 14, 92, 37]
for num in bar:
	if num%2 == 0:
		foo.append(num)

#and replace it with this:
bar = [1, 17, 8, 83, 26, 11, 14, 92, 37]
foo = [num for num in bar if num%2 ==0]
print(foo)

#What if we want to return a list with the even elements of bar doubled?


'''
BREAKOUT EXERCISE:

#1. Find a way to represent a two dimensional array using just lists.
Example: an array with 3 rows and 3 columns like

1 2 3
4 5 6
7 8 9


#2. Write a function that takes this data structure, a row number
    and a column number as input and returns the value in that array
    that corresponds to the given row and column. The skeleton of the
    code should look like this:

def array_indexer(data, row_num, col_num):

	#BODY OF FUNCTION#

	return(value)

	For example, if I passed the data above along with row_num = 0
	and col_num = 1, I should return the value 2.

#3. If you have time left, write a function that takes this same type
    of data structure as well as a number, and returns True if the number
    is in the array. What code could we add to make sure we don't keep searching
    once we've found the number? How could you count the number of times the number
    appears? 
'''




##### Object Oriented Programming #####

'''
Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new 
instances of that type to be made. Each class instance can have 
attributes attached to it for maintaining its state. Class instances 
can also have methods (defined by its class) for modifying its state.
			- Python Docs: https://docs.python.org/3/tutorial/classes.html
'''

class Dog:

    def __init__(self, name):
        self.name = name
        self.breed = ''
        self.age = 0
        self.fed_status = 'Not fed'

    def have_birthday(self):
    	self.age += 1

    def feed(self, food):
    	new_fed_status = self.name + ' has been fed with ' + food
    	self.fed_status = new_fed_status

my_dog = Dog('Spot')

print(my_dog.name)
print(my_dog.age)
print(my_dog.fed_status)

my_dog.feed('pizza')

print(my_dog.fed_status)

my_dog.have_birthday()

print(my_dog.age)


# Note that we can get as complex as we want with the underlying data structure
# When someone interacts with an instance of our class, they could be dealing with
# lists, dictionaries, or dataframes without even knowing it!


class Candidate:

	def __init__(self):
		self.name = ''
		self.party = ''
		self.states_dict = {}

	def win_state(self, state, votes):
		self.states_dict[state] = votes

	def has_won(self):
		electoral_votes = sum(list((self.states_dict).values()))
		return(electoral_votes >= 270)



'''
BREAKOUT EXERCISE:

Play around with this class. Instantiate it. Give your candidate
a name and a political party. Give them some states either by
setting states_dict to a pre built dictionary or by using win_state.
Check if they've won the election.
Give them a new state with enough votes to win the election, and then 
check again to see if they've won.
'''



########## Pandas & Sklearn ###########


# A 'machine learning' work flow:

#1. Import csv data as pandas df, clean
#2. Train/test split
#3. Instantiate model object and define parameter grid
#4. Instantiate GridSearchCV object
#5. Fit data (do grid search)
#6. Examine best parameters and score
#7. Predict on test set
#8. Evaluate predictions

import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn import svm
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score

## 1. Import csv as pandas df, clean ##
data = pd.read_csv('https://raw.githubusercontent.com/SohailNizam/INFO550-Py/main/Titanic.csv')

#take a look
print(data.head())
print(data.columns)

#drop passenger id, cabin, name, ticket
data = data.drop(columns = ['PassengerId', 'Cabin', 'Name', 'Ticket'])
#dummy code sex and embarked
data = pd.get_dummies(data, columns = ['Sex', 'Embarked'])
print(data.head())
#drop na values
data = data.dropna()


## 2. Train/test split ##
X = data.drop(columns = ['Survived'])
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

## 3. Instantiate model object and define parameter grid ##
svc = svm.SVC()
param_grid = {'C' : [1, 5], 'kernel' : ['linear', 'rbf']}

## 4. Instantiate a GridSearchCV object ##
svm_grid_search = GridSearchCV(estimator = svc, param_grid = param_grid, 
	scoring = 'accuracy', cv = 2, refit = True)

## 5. Fit data (do grid search) ##
svm_grid_search.fit(X_train, y_train)

## 6. Examine best parameters and score ##
print(svm_grid_search.best_params_)
print(svm_grid_search.best_score_)


## 7. Predict on test set ##
preds = svm_grid_search.predict(X_test)

## 8. Evaluate predictions ##

#test prediction accuracy
print('Accuracy:')
print(accuracy_score(y_test, preds))
print()

#test prediction f1
print('F1:')
print(f1_score(y_test, preds))
print()

#test prediction AUC
print('AUC:')
print(roc_auc_score(y_test, preds))





