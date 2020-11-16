#Check the python version you're using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


######### Some Basic Commands #########

print('Hello World!')

print(3 + 3)


'''
multi line
comment

'''

############# Data Types ##############

print(type(3))

print(type(3.0))

print(type('hello'))

print(type(True))

print(type(3 == 3))



########### Data Structures ###########

#List Facts:
#1. Lists are mutable (can be modified in place)
#2. Lists can contain many differeny data types all at once
#3. Lists can be indexed and sliced
#4. We cannot perform elementwise operations on lists like R vectors


# Lists ##
foo = [1, 2, 3]

bar = ['a', 'b', 'c']

baz = [16, 'apple', 17.4, True]

print(foo, bar, baz)

print(type(foo))

print(foo[0])

print(bar[1:3])

foo[1] = 'a'
print(foo)

## Sets ##

#Set Facts:
#1. Sets are unordered
#2. Sets cannot be indexed or sliced
#3. Sets have unique elements
#4. list(set(mylist)) is a very pythonic way to get a list with unique elements


new_set = {1, 2, 1, 2, 3, 4, 1}

print(new_set)

foo_set = set(foo)

print(foo_set)

print(foo_set[0])

# MINI BREAKOUT: Find out why the line directly above doesn't work.

# Question: How can we get the unique elements of a list? #
l = [1, 1, 2, 3]
print(list(set(l)))


# Dictionaries #

#Dictionary Facts:
#1. Dictionaries are made up of key value pairs
#2. Below, state names are the keys and electoral votes are the values
#3. Dictionaries allow for fast lookup of values by key names
#4. Keys and values can be any data type
#4b. We could build a recursive data structure by creating a dictionary with values that are dictionaries
#5. We can access the keys and values separately using the .keys() and .values() methods

state_dict = {'Pennsylvania' : 20,
              'Arizona' : 11,
		      'Georgia' : 16,
		      'Nevada' : 6,
		      'Michigan' : 16,
		      'Wisconsin' : 10}

print('Georgia has', state_dict['Georgia'], 'Electoral Votes')

print(list(state_dict.keys())

print(state_dict.values())


############# Conditionals ############

#These don't differ much from R except that
#we've given up {} and () for indents

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
for apple in range(10):
	print('hi')

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

#SOLUTION:
#Iterate over keys using: for key in my_dict.keys()
#Iterate over values using: for val in my_dict.values()
#Iterate over both using: for key, val in my_dict.items()



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
	if (val[0] > 10) and  val[1] == 'South':
		print(key, 'is a key southern state.')


# #How could I quickly modify the code above to include Southwestern states?
# #I can think of 2 ways...

#1.
for key, val in state_dict.items():
	if val[0] > 10 and (val[1] == 'South' or val[1] == 'Southwest'):
		print(key, 'is a key southern state'.) 
	

#2.
#the 'in' operator works for strings just like for lists
#pay attention to cases though!
#best practice is to lowercase everything. e.g.:
# if substring.lower() in string.lower()
for key, val in state_dict.items():
	if val[0] > 10 and 'South' in val[1]:
		print(key, 'is a key southern state'.)
	 


############# While Loops #############

#Again, these are just like in R.
#Indents instead of {} and ()

#When to use a while loop?
#Keep iterating until a condition is met.
#Let's use a while loop to compute a factorial
num = 5
fac = 1
while num > 1:
	fac *= num
	num -= 1

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

#Once again, indents are everything

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

#We'll do it using lambda expressions
#a lambda expression is an anonymous function
#it does not have a name and will not exist outside of the scope
#it's being defined in
#The structure is:
# lambda arg1, arg2, ..., argn: <fcn body>

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
foo = [num for num in bar if num%2 == 0]
print(foo)


#What if we want to return a list with the even elements of bar doubled?
foo = [2*num for num in bar if num%2 == 0]


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

# Solution
#1. use a list of lists: [[1,2,3], [4,5,6], [7,8,9]]
#2.

def array_indexer(data, row_num, col_num):
	target_num = data[row_num][col_num]
	return(target_num)



#3.

def has_num(data, num):
	#initialize a variable 'has' to False
	#We'll only change it to true if we find our number
	has = False
	for sublist in data:
		for item in sublist:
			if num == item:
				#If we find our number, switch to true
				has = True
				#Break because once we've found our number
				#we're done!
				break

	#return a boolean
	#this will enable us to write code like:
	#if has_num(data, num): ...
	return(has)

#we could simplify this solution by removing a for loop as follows:

def has_num_efficient(data, num):
	has = False
	for sublist in data:
		if num in sublist:
			has = True
			break
	return()


#Now how to count the occurences? We don't want break anymore.
#And we'll need a counter variable.

def count_occurences(data, num):
	counter = 0
	for sublist in data:
		for item in sublist:
			if num == item:
				counter += 1
	return(counter)


##### Object Oriented Programming #####

'''
Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new 
instances of that type to be made. Each class instance can have 
attributes attached to it for maintaining its state. Class instances 
can also have methods (defined by its class) for modifying its state.
			- Python Docs: https://docs.python.org/3/tutorial/classes.html


This is a new way to create, store, access, and update data.
Data does not just have to be a matrix of rows and columns.
We can store it in a more abstract way that is specific to our needs.
Can reduce the need for spaghetti code (fcn1 calls fcn2 calls fcn3, ....)
Can make it easier for users of your code who don't want to understand
the complex function structure you've written.
Can make it easier to add new features to your analysis and manage existing ones.

Also, python is object oriented whether we program that way or not.
Everything is a python object. Lists, dicts, sets, ints, floats. They're all
objects. When we create a lists l = [1, 2, 3], we create an instance of the list class.
That class, no matter what data is inside, has attributes and methods associated with it
so that you can do all of the tasks you might want in a convenient way.
'''


#this is a class that store information about a dog.
#we can populate this class with whatever info you want.
#think of this as a blueprint for your very own, specific data object: Dog.
#I can create a dog named Spot who is a beagle and has just been fed pizza
#Or I can create a dog named Air Bud who is a golden retriever and has not been fed.
#Just like I can create a list l1 = [1, 2, 3] or another list l2 = [4, 5, 6]
#I can update things about the dog like increasing its age with my_dog.have_birthday() 
#just like I can update l1 by appending a value with l1.append(8)
class Dog:

    def __init__(self, name):
    	#name, breed, age, and fed_status are attributes
    	#attributes go in this special __init__ function at the top
        self.name = name
        self.breed = ''
        self.age = 0
        self.fed_status = 'Not fed'

    #have_birthday() and feed(food) are methods
    #methods are functions specific to this new data type we defined
    #write any methods you think a user would need to manage their dog data
    def have_birthday(self):
    	self.age += 1

    def feed(self, food):
    	new_fed_status = self.name + ' has been fed with ' + food
    	self.fed_status = new_fed_status

#Create a dog named spot
my_dog = Dog('Spot')

#Check all of Spot's current attributes
print(my_dog.name)
print(my_dog.age)
print(my_dog.fed_status)

#use the feed method.
my_dog.feed('pizza')

#check the fed_status attribute again
print(my_dog.fed_status)

#use the have_birthday() method
my_dog.have_birthday()

#check the dog's age attribute again
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

'''
Why make these classes? Instead of having to write function calls over and over
to find out information about our object, update our object, perform operations on it
etc, the data and all the useful tasks associated with it are all neatly wrapped up. 
'''

########## Pandas & Sklearn ###########

'''
Here's a nice example of a a work flow in python where the fact that python 
is built on OOP really becomes obvious. We'll deal with model objects, use
methods to fit them, use more methods to predict outcomes with new data using them.

We'll see that pandas (how we do R-like stuff in python) is built around a DataFrame
object which has many useful methods and attributes. 

Want to find out the dimensions of a dataframe? Don't write code to count the rows! DataFrame
objects have an attribute called shape. The info is already there because python knows we'll
want it.

Want to drop a column? Don't write code to slice the df or select all columns but one. DataFrame
objects have a method called drop. That capability is already there beceaus python knows we'll
want it.
'''


# A 'machine learning' work flow:

#1. Import csv data as pandas df, clean
#2. Train/test split
#3. Instantiate model object and define parameter grid
#4. Instantiate GridSearchCV object
#5. Fit data (do grid search)
#6. Examine best parameters and score
#7. Predict on test set
#8. Evaluate predictions

#pandas is a library for managing dataframes in an R like way
import pandas as pd
#sklearn (sci-kit learn) is a full suite for all of your
#off the shelf machine learning needs
#Here I import modules for doing a cross validated grid search
#and for splitting my data into a train/test set
from sklearn.model_selection import GridSearchCV, train_test_split
#Here I import a module for creating support vector machine fits
from sklearn import svm
#Here I import modules for evaluating my model
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score

## 1. Import csv as pandas df, clean ##
#read_csv is just like read.csv in R. Be sure to specify things like header=True/False
#read the docs to see what argument defaults are
#read_csv works for links or for local file paths
data = pd.read_csv('https://raw.githubusercontent.com/SohailNizam/INFO550-Py/main/Titanic.csv')

#take a look
#first we view the first few rows in the dataset
#.head() is a method available specifically for the pd.DataFrame object
print(data.head())
#Here I print the columns names
#.columns is an attribute of the pd.DataFrame object`
print(data.columns)

#** Can't remember what methods and attributes are? Either go to the official docs or see this stackexchange link:
#https://stackoverflow.com/questions/46312470/difference-between-methods-and-attributes-in-python#:~:text=Methods%20are%20functions%20that%20belong,exercise%20is%20likely%20talking%20about.&text=A%20method%20is%20a%20function,variable%20defined%20in%20the%20class.

#drop passenger id, cabin, name, ticket
#again, .drop() is a method for pd.DataFrame objects. We can drop any columns we wany by name
#names are passed as strings in a list as shown below.
data = data.drop(columns = ['PassengerId', 'Cabin', 'Name', 'Ticket'])
#dummy code sex and embarked
#get_dummies is also a method for pd.DataFrame objects
#we turn categorical variables with k levels into k-1 0/1 columns
data = pd.get_dummies(data, columns = ['Sex', 'Embarked'])
print(data.head())
#drop na values
#another method! This drops rows with na values
data = data.dropna()


## 2. Train/test split ##

#let's drop the outcome (Survived) to create our design matrix
X = data.drop(columns = ['Survived'])
#let's isolate the outcome to create our outcome column
#** A single column in pandas is called a Series (pd.Series object)
y = data['Survived']
#Here we use our imported splitting module to split our data
#into train and test sets. This uses stratified splitting
#to preserve the proportion of y=1 in both train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

## 3. Instantiate model object and define parameter grid ##
#First we create an empty svm model object
#We'll be able to fit it to data later
svc = svm.SVC()
#use a dictionary with hyper-parameter keys (as defined by the sklearn docs)
#and list values. The lists should contain all of the parameter values
#you want to try.
#When we pass this grid, GridSearchCV will do cross validation
#on every single combination of the parameter values below
#and return the best one in terms of your chosen metric
param_grid = {'C' : [1, 5], 'kernel' : ['linear', 'rbf']}

## 4. Instantiate a GridSearchCV object ##
#here's an empyt GridSearchCV object
#It has many of the same methods and attributes as an smv.SVC() object
#This, in essence, has become our model.
#We will fit this instead of fitting the svm directly
svm_grid_search = GridSearchCV(estimator = svc, param_grid = param_grid, 
	scoring = 'accuracy', cv = 2, refit = True)

## 5. Fit data (do grid search) ##
#if we didn't want to do a grid search
#we could just use:
#svc.fit(X_train, y_train)
svm_grid_search.fit(X_train, y_train)

## 6. Examine best parameters and score ##
#best_params_ and best_score are attributes of a
#GridSearchCV object
print(svm_grid_search.best_params_)
print(svm_grid_search.best_score_)


## 7. Predict on test set ##
#.predict() is a method for a model object
#as we've said, models come in many forms
#it could be an svm.SVC() model object
#could be a RandomForrestClassifier() object
#In this case, our model object is a GridSearchCV object
#After choosing the best params, GridSearchCV uses those
#and fits all of the data so it can be used directly as a model
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





