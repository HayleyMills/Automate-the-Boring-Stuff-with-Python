##Write a function named printTable() that takes a list of lists of strings
##and displays it in a well-organized table with each column right-justified.
##Assume that all the inner lists will contain the same number of strings.
##For example, the value could look like this:

##tableData = [['apples', 'oranges', 'cherries', 'banana'],
##             ['Alice', 'Bob', 'Carol', 'David'],
##             ['dogs', 'cats', 'moose', 'goose']]

##Your printTable() function would print the following:
##
##  apples Alice  dogs
## oranges   Bob  cats
##cherries Carol moose
##  banana David goose

#def printTable():
    #input is a list of strings
    #output is an orgniased table with each column rjust


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


rows = len(tableData) #number of lists 
cols = len(tableData[0]) #number of cols 

maxlength = 0

for i in range(0,(rows)): #loop for number of rows
    for x in tableData[i]: #loop for the each item in the row
        if maxlength < len(x): #find the max length of the words
            maxlength = len(x)

for k in range(0, (cols)):
    for v in range(0, (rows)):
        print((tableData[v][k]).rjust(maxlength), end = ' ')
    print()


        
