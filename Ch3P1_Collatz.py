#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. 
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. 
#(Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! 
#Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)


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
