#Write a function that takes a list value as an argument and returns a string
#with all the items separated by a comma and a space, with and inserted before
#the last item. For example, passing the previous spam list to the function
#would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.

def andThis(lyst):
    if type(lyst) is list:
        for item in range(len(lyst)):
            if item == (len(lyst))-1:
                print ('and ' + lyst[item]) 
            else:
                print (lyst[item] + ',' , end= " ")
    else:
        print("Please use a list")

spam = ['apples', 'bananas', 'tofu', 'cats']
test = 'string'

andThis(test)
