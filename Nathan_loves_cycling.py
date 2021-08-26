#Nathan loves cycling. Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of
#water per hour of cycling. You get given the time in hours and you need to return
#the number of litres Nathan will drink, rounded to the smallest value.
#1.	Try to incorporate error handling into your function. For example, what if I enter a string? 
#2.	How might I round to the higher value instead of the lower one? 


def waterHoursCycle():
    hours = input('How many hours cycling?')

    try:                    #convert string to int or float
        hours = int(hours)
    except ValueError:
        hours = float(hours)


    if hours <0:
        print('You need to enter a positive number')
    else:
        hours = print('You need to drink at least ' + str(int(hours/0.5)) + ' litres of water')
    
#not sure how to add what to do if they enter characters instead of numbers?


waterHoursCycle()
