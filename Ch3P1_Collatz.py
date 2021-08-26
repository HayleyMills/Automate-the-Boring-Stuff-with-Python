def collatz(number):
    try:
        if number % 2 == 0:
            number2=number//2
            print(str(number) + ' // 2 = ' + str(number2))
            #return number2
            
        else:
            number3 = 3 * number + 1
            print('3 * ' + str(number) + ' + 1 = ' + str(number3))
            #return number3
        
    except ValueError:
        print("Please enter an integer")
        
number4=input("Enter an interger ")
try:
    while int(number4) > 1:
        number4 = collatz(int(number4))
        
except ValueError:
    print("Please enter an integer")

collatz(10)
