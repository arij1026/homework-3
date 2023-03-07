#!/usr/bin/env python
# coding: utf-8

# # Jypyter Notebooks and Python Refresh Homework 3
# We are going to do the Python Refresh Homework in a juypyter Notebook. In this homework we will review the basic principles of python programming. You will work through a few questions and build some scripts. You will need the Bloom et al Dataset found in this repository. For each question add a cell to put your answer in either as a text cell or a code cell following the question.
# 
# ### Markdown
# Here is a [markdown refresh](https://programminghistorian.org/en/lessons/getting-started-with-markdown)
# 
# ### General concepts to refresh and lessons to review if you need them:
# 
# Here is a nice [Python_Refresh](https://pythonforbiologists.com/introduction) that goes over the majority of the basic python commands.
# 
# Remember these Primers from Last Semester
# 
# [Python_Primer1](https://github.com/tparchman/BIOL792_course_site/blob/master/week6_pythonI/python_1_primer.md) 
# 
# [Lists_for_loops](https://github.com/tparchman/BIOL792_course_site/blob/master/week7_pythonII/python_2_primer.md)
# 
# [Input_Output](https://github.com/tparchman/BIOL792_course_site/blob/master/week8_python3/python_3_primer.md)
# 
# [Dictionaries](https://github.com/tparchman/BIOL792_course_site/blob/master/week11_python6/primer_python6.md)
# 
# 
# ### Remember these Common commands as you work through this exercise
# 	data types
# 	lists and dictionaries 
# 	if while and for loops
# 	reading files
# 
# 

# In[1]:


3+3


# This is text

# In[ ]:





# ## Part I: Questions

# 1.	Name one of the basic building blocks of programming and a small definition.

# Arguments are values that are sent to the program when it is run

# 2.	Match the data type to the appropriate data
#     
#     **Data type:** string, integer, boolean, floating point
#     
#     **Data:** true, 123, 'I am a programmer', 34.63221
# 

# integer - 123
# floating point - 34.63221
# Boolean - true
# string - i am programmer

# 3.	What would I get if I did tried to add these to numbers together ```123``` and ```5```.
# 		
# 		a) if the numbers were formatted as strings
# 		
# 		b) if they were formatted as integers

# a) 'one hundred twenty three and five'
# b) 128

# 4.	Lists, also called vectors, are one dimensional arrays and are a series of items. From the following list what would the question ```apple_list[3]``` return?  Remember we refer to items in a list by their position. Hint – remember how computers count.
# 		
# 		```apple_list=[‘banana’,’pear’,’kumquat’,’pomegranate’,’passion fruit’]```

# pomegranate

# 5.	Name a difference between lists and dictionaries?

# Dictionaries are unordered, so they ask for values according to their keys and not positional arguments like a list

# 6.	What would you get from this question from the following dictionary:  ```fruit_dict[‘pear’]```
# ```		
# 		fruit_dict = {}
# 		fruit_dict[‘apple’]=10
# 		fruit_dict[‘pear’] = 3
# 		fruit_dict[‘walnut’]=216
# ```
# or in another way
# 
# 
# ```
# fruit_dict = {
#     'apple':10,
#     'pear':3,
#     'walnut':216,
# }
# 
# print(fruit_dict)
# ```
# 
# 

# a) 3
# b) {'apple': 10, 'pear': 3, 'walnut': 216}

# 7.	In python what does the function ```.replace()``` do?

# It searches a certain string for a specified character(s) and returns a new string where the specified character(s) are replaced

# 8.	How do you print something in python?  For example write a print statement to print “hello world!”

# In[12]:


print('hello world!')


# 9.	Name one place you can go to get help with python?

# In[ ]:


Github


# 10.	What is an ```if``` statement and when would you use one?

# An 'if' statement evaluates an if statement and returns a Boolean. If it is true, it execites a series of commands. You would use one if dealing for species names, for example. Or, when dealing with a range of numbers. Essentially, if you are faced with a fork in the road with what you want to do with your ocde, an if statement is useful.

# 11.	From this list:  ```container_list = [‘can’,’jar’,’hat’]``` What would be returned from this: ```container_list[0:2]```.  Hint: Remember one number is inclusive and one exclusive.

# ['can', 'jar']

# 12.	What is the difference between an ```if``` statement and a ```while``` loop?
# 

# An if statement executes a aeries of commands if parameters are true, and a while loop executes until a condition is met.

# 13.	What would you get with the command ```fruit_dict.keys()```  after entering this dictionary:  
# 		fruit_dict = {}
# 		fruit_dict[‘apple’]=10
# 		fruit_dict[‘pear’] = 3
# 		fruit_dict[‘walnut’]=216

# In[ ]:


dict_keys(['apple', 'pear', 'walnut'])


# 14.	In this statement: ```InFileName = open(InFileName, ‘r’)``` what does the ‘r’ indicate ?

# It indicates the mode of operation. 'r' is short for read

# 15.	What does this command do? ```Line.strip(‘\n’)``` why would you use it when printing out lines to the screen?

# This command removes a line ending. You would use thise for printing out lines to the screen if you want to get ride of the white space at the end of the line. 

# 16.	How would you split a line from a csv file into a list

# In[ ]:


I could use Line.split('\t')


# ## Part II:  Practice Scripts
# Below each question write the name of the script so I can find them. All scripts should be documented with in-line documentation.

# 1.	Create a documented python script that would 
# 
# 		**a.** take this number 112345678911234566 and count the number of 2s in the string and print out the number. 
# 
# 		**b.** take a sentence from user input, turn it all to lowercase letters and remove the spaces and count the length and print out the length.  You choose the sentence. 
# 

# In[25]:


str1 = '112345678911234566' ## create the string

str1_count = str1.count('2') ## count how many times 2 shows up

print(str1_count) ## print how many times 2 appears in the string


# In[26]:


## create function to remove spaces and replace upper case with lower case
def removeSpaces(str2): 
    str2 = str2.replace(' ','')
    str2 = str2.lower()
    return str2

str2 = "I Am Sick of All This Snow" ## create string and driver program
print(removeSpaces(str2))

len(str2) ## count characters


# 2.	Create a documented python script that will do the following two things. For each task, first write the pseudocode, comment out the pseudocode and beneath the pseudocode write the script.
# 
# 		**a.** Create a list of numbers (any numbers you like). Then loop through the items in the list adding 1 to every number and print those numbers.
# 
# 		**b.** Create a dictionary of animals and their sizes (make up whatever you want). Print out the keys of the dictionary. Make a list of all the animals and then write an if else statement to print out the animal name and the word “big” if the weight is over 20 grams and the word “small” if the weight is less than 20 grams. 

# In[27]:


## pseudocode: I want to create a list of numbers, open a loop, take each number and add one, put that into a list, then print that list.
list = [1, 4, 9, 16, 25] ## create number list

## for loop to add 1 to each number
for i in list:
    list = i + 1
    print(list)


# In[35]:


## pseudocode: I want to create a dictionary, pull variables, establish a breakpoint for weight, create an if else statement that classifies animals as small or big

##create dictionary
dict = {
    'cow':100,
    'cat':25,
    'mouse':8,
    'hamster':10}

## pull out variables
break_pt = 20
grams = dict.values()
animal = dict.keys()

#if else statement
for animal, grams, in dict.items():
    if grams > break_pt:
        print(animal,'is', 'big')
    elif grams < break_pt:
        print(animal, 'is', 'small')
    else:
        pass
        


# 3.	Create a documented python script that will open up the file “Bloom_etal_2018_Reduced_Dataset”.  Read through the file and print out the taxon name and their diadromous status. Add up all of the log body sizes and print out the total log body size for all the individuals in the file.  

# In[78]:


## pseudocode: I want to open a file, read and print out each taxon name with diadromous status, then print the sum of the total log body size

## open the file and print name with status
import csv
with open('Bloom_etal_2018_Reduced_Dataset.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print("The taxon name is {} and their status is {}.".format(row[0], row[3]))


# In[100]:


## print sum of body log sizes
import pandas as pd
df = pd.read_csv('Bloom_etal_2018_Reduced_Dataset.csv')
body_sum = df['logbodysize'].sum()
print(body_sum)


# In[ ]:




