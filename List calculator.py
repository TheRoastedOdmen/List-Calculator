from time import sleep
from math import factorial
#import numpy

u = '\nL I S T   C A L C U L A T O R\n'
print('#' * ((len(u)) - 2))
print(u)
print('#' * ((len(u)) - 2))

print('\nFirstly choose an option\n'
    'Then input the numbers via enter\n'
    'When you done inputting press enter to get the results\n'
    'Note that you can input any amount of numbers\n')

log = open('calculator_log.txt', 'w')
rn = 15 #rounding

while True:
    try:
        print("\n__________OPTIONS___________ \n"
            "\nInput '+' to sum the numbers\n"
            "Input '-' to substract the numbers\n"
            "Input '*' or 'x' to multiply the numbers\n"
            "Input '/' to divide the numbers\n"
            "Inpur 'a' or 'average' to find the average number\n"
            "Input '**' or '^' to exponentiation of the numbers\n"
            "Input 'y/x' to divide the one number to a list of numbers (also %)\n"
            "Input 'x/y' to divide a list of number to the one number (also %)\n"
            "Input '!' to factorial the numbers\n"
        #    "Input 'openlast' to see the last result\n"
            "Input 'ol' or 'openlog' to see the log of the session\n"
            "Input 'r' or 'round' to set the rounding number of the results\n"
            "\nInput 'exit' to quit the program")

        log = open('Calculator_log.txt', 'a')
        a = str(input("\nChoose an option: ")).lower()
        n = 1
        y = []
        t1 = []
        y1 = 0
        y2 = 0
        #np.seterr(divide='ignore')

        if a == "exit":
            break


#Rounding module

        elif a == 'round' or a == 'rounding' or a == 'r':
            print("\nYou can set the rounding number for the results\n"
                "0 will round results to the integer,\n"
                "1 - to the first number after integer, e.t.c.\n"
                "15 is by default\n")
            print('Active rounding number is', rn, '\n' )            
            rn = int(input('Enter the rounding number: '))
            print("New rounding number is set to ", rn, '\n')

            log.write('\n')
            log.write('The rounding number is set to ')
            log.write(str(rn))
            log.write('\n')

            sleep(0.75)


#Addition module

        elif a == '+':
            print('\nYou have choosen the Addition\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            y1 = str(round(sum(y), rn))
            
            u1 = 'Addition result: '
            print()
            print('+' * (len(u1) + len(y1) + 1), '\n')
            print(u1, y1, '\n')
            print('+' * (len(u1) + len(y1) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('+')
            file.write('\n\nLast ')
            file.write(u1)
            file.write(y1)
            file.write('\n+')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write(y1)
            log.write('\n')

            sleep(1)


#Substraction module

        elif a == '-':
            print('\nYou have choosen the Substraction\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            def m1():
                y1 = y[0]
                for x in y[1:]:
                    y1 += -x
                return round(y1, rn)

            u1 = 'Substraction result: '
            print()
            print('-' * (len(u1) + len(str(m1())) + 1), '\n')
            print(u1, m1(), '\n')
            print('-' * (len(u1) + len(str(m1())) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('-')
            file.write('\n\nLast ')
            file.write(u1)
            file.write(str(m1()))
            file.write('\n-')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write(str(m1()))
            log.write('\n')

            sleep(1)


#Multiplication module

        elif a == '*' or a == 'x':
            print('\nYou have choosen the Multiplication\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)
            
            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            def m1():
                y1 = 1
                for x in y:
                    y1 = y1 * x
                return round(y1, rn)

            u1 = 'Multiplication result: '
            print()
            print('x' * (len(u1) + len(str(m1())) + 1), '\n')
            print(u1, m1(), '\n')
            print('x' * (len(u1) + len(str(m1())) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('x')
            file.write('\n\nLast ')
            file.write(u1)
            file.write(str(m1()))
            file.write('\nx')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write(str(m1()))
            log.write('\n')

            sleep(1)


#Division module

        elif a == '/':
            print('\nYou have choosen the Division\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)

                    
                except:
                    break

            def m1():
                y1 = y[0]
                for x in y[1:]:
                    y1 = y1/x
                return round(y1, rn)

            u1 = 'Division result: '
            print()
            print('/' * (len(u1) + len(str(m1())) + 1), '\n')
            print(u1, m1(), '\n')
            print('/' * (len(u1) + len(str(m1())) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('/')
            file.write('\n\nLast ')
            file.write(u1)
            file.write(str(m1()))
            file.write('\n/')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write(str(m1()))
            log.write('\n')

            sleep(1) # TODO: Program has to delete x = 0 value and continue
                     #       to append(x) (same to y/x and x/y)


#Average number Module

        elif a == 'average' or a == 'a':
            print("\nYou have choosen the Average number\n")
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:--->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            y1 = str(round((sum(y)/len(y)), rn))

            u1 = 'Average number result: '
            print()
            print('=' * (len(u1) + len(y1) + 1), '\n')
            print(u1, y1, '\n')
            print('=' * (len(u1) + len(y1) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('=')
            file.write('\n\nLast ')
            file.write(u1)
            file.write(y1)
            file.write('\n=')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write(y1)
            log.write('\n')

            sleep(1)


#List calculator modules

#Exponentiation module

        elif a == '**' or a == '^':
            print('\nYou have choosen the Exponentiation\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            v = float(input('Enter the exponent: '))
            print('\nExponent:--->', v)
         
            def m1():
                for x in y:
                    y1 = x**v
                    yield str(round(y1, rn))
            
            for y1 in m1():
                t1.append(y1)

            u1 = 'Exponentiation result: '
            print()
            print('^' * (len(u1) + len(max((t1), key=len)) + 1), '\n')
            for y1 in m1():
                print(u1, y1, '\n')
            print('^' * (len(u1) + len(max((t1), key=len)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('^')
            file.write('\n\nLast ')
            file.write(u1)
            file.write('\n')
            for y1 in m1():
                file.write(str(y1))
                file.write('\n')
            file.write('\n^')
            file.close()

            log.write('\n')
            log.write(u1)
            log.write('\n')
            for y1 in m1():
                log.write(str(y1))
                log.write('\n')
            log.write('\n')

            sleep(1)


#y/x module

        elif a == 'y/x':
            print('\nYou have choosen the y/x\n')
            z = float(input('Enter the main number (y): '))
            print('Main number (y): ', z)
            x = float(input('Enter the number (x): '))
            print(str(n) + 'st number (x): ',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number (x): '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number (x): ',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number (x): ',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number (x): ',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number (x): ',x)
                except:
                    break

            def m1():
                for x in y:
                    y1 = z/x
                    yield str(round(y1, rn))

            for y1 in m1():
                t1.append(y1)
          
            u1 = 'y/x result: '
            print()
            print('^' * (len(u1) + len(max((t1), key=len)) + 1), '\n')
            for y1 in m1():
                print(u1, y1, '\n')
            print('^' * (len(u1) + len(max((t1), key=len)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('//')
            file.write('\n\nLast ')
            file.write(u1)
            file.write('\n')
            for y1 in m1():
                file.write(str(y1))
                file.write('\n')
            file.write('\n//')

            log.write('\n')
            log.write(u1)
            log.write('\n')
            for y1 in m1():
                log.write(str(y1))
                log.write('\n')
            log.write('\n')

            #y/x % result

            def m2():
                for y1 in m1():
                    y2 = str(float(y1)*100) + ' %'
                    yield y2

            u2 ='y/x % result: '
            print()
            print('%' * (len(u2) + len(max((str(float(y1)*100) for y1 in m1()), key=len)) +3), '\n')
            for y2 in m2():
                print(u2, y2, '\n')
            print('%' * (len(u2) + len(max((str(float(y1)*100) for y1 in m1()), key=len)) +3))

            file.write('\n\n\n%')
            file.write('\n\nLast ')
            file.write(u2)
            file.write('\n')
            for y2 in m2():
                file.write(str(y2))
                file.write('\n')
            file.write('\n%')
            file.close()

            log.write('\n')
            log.write(u2)
            log.write('\n')
            for y2 in m2():
                log.write(str(y2))
                log.write('\n')
            log.write('\n')

            sleep(1)


#x/y module

        elif a == 'x/y':
            print('\nYou have choosen the x/y\n')
            x = float(input('Enter the number (x): '))
            print(str(n) + 'st number (x): ',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number (x): '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number (x): ',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number (x): ',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number (x): ',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number (x): ',x)
                except:
                    break

            z = float(input('Enter the division number (y): '))
            print('Division number (y): ', z)

            def m1():
                for x in y:
                    y1 = x/z
                    yield str(round(y1, rn))
           
            for y1 in m1():
                t1.append(y1)

            u1 = 'x/y result: '
            print()
            print('^' * (len(u1) + len(max((t1), key=len)) + 1), '\n')
            for y1 in m1():
                print(u1, y1, '\n')
            print('^' * (len(u1) + len(max((t1), key=len)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('//')
            file.write('\n\nLast ')
            file.write(u1)
            file.write('\n')
            for y1 in m1():
                file.write(str(y1))
                file.write('\n')
            file.write('\n//')

            log.write('\n')
            log.write(u1)
            log.write('\n')
            for y1 in m1():
                log.write(str(y1))
                log.write('\n')
            log.write('\n')

            #x/y % result

            def m2():
                for y1 in m1():
                    y2 = str(float(y1)*100) + ' %'
                    yield y2

            u2 ='x/y % result: '
            print()
            print('%' * (len(u2) + len(max((str(float(y1)*100) for y1 in m1()), key=len)) +3), '\n')
            for y2 in m2():
                print(u2, y2, '\n')
            print('%' * (len(u2) + len(max((str(float(y1)*100) for y1 in m1()), key=len)) +3))

            file.write('\n\n\n%')
            file.write('\n\nLast ')
            file.write(u2)
            file.write('\n')
            for y2 in m2():
                file.write(str(y2))
                file.write('\n')
            file.write('\n%')
            file.close()

            log.write('\n')
            log.write(u2)
            log.write('\n')
            for y2 in m2():
                log.write(str(y2))
                log.write('\n')
            log.write('\n')

            sleep(1)


#Factorial module

        elif a == '!':
            print('\nYou have choosen the Factorial\n')
            x = int(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = int(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            #vaule error skipping is needed

            def m1():
                for x in y:
                    y1 = factorial(x)
                    yield y1
            
            u1 = 'Factorial result: '
            print()
            print('!' * (len(u1) + len(max((str(factorial(x)) for x in y), key=len)) + 1), '\n')
            for y1 in m1():
                print(u1, y1, '\n')
            print('!' * (len(u1) + len(max((str(factorial(x)) for x in y), key=len)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('!')
            file.write('\n\nLast ')
            file.write(u1)
            file.write('\n')
            for y1 in m1():
                file.write(str(y1))
                file.write('\n')
            file.write('\n!')    
            file.close()

            log.write('\n')
            log.write(u1)
            log.write('\n')
            for y1 in m1():
                log.write(str(y1))
                log.write('\n')
            log.write('\n')

            sleep(1)


#Log modules

        elif a == 'openlast':
            print('\nPrinting the last result: ', '\n')
            file = open('last_calculator_result.txt', 'r')
            print(file.read())
            file.close()

            sleep(1)

        elif a == 'openlog' or a == 'ol':
            print('\nPrinting the last session of the calculator log: ')
            sleep(0.5)
            log = open('Calculator_log.txt', 'r')
            print(log.read())

            sleep(1)


        else:
            q = 'Unknown input'
            print()
            print('?' * (len(q)))
            print(q)
            print('?' * (len(q)))

            sleep(0.75)

    finally:
        log.close()

#TODO:
#division by zero
#unknown inputs in x
#dates in python log
#what was calculating in logs
#modules and decorators
#rounding to 0 and y/x x/y roundings (output symbols, watch for **)
#lambdas
#random func