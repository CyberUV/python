print("Here You Can Calculate Everything Created BY Rudraksh Yadav")
print("------------------------------------------------------------------------------ \n")

def calculate() :
    a = float(input("Enter Your First Number ==> "))
    b = float(input("Enter Your Second Number ==> "))
    ope = input("press + - * / for operation and type esc for exit ==> ")

    print()

    if ope == "+" :
        print(f'Question ==> {a} {ope} {b} ')
        print(f'Answer is {a + b}')
        print("------------------------------------------------------------------------------")
        print()
        calculate()
        
    elif ope == "-" :
        print(f'Question ==> {a} {ope} {b} ')
        print(f'Answer is {a - b}')
        print("------------------------------------------------------------------------------")
        print()
        calculate()
        
    elif ope == "*":
        print(f'Question ==> {a} {ope} {b} ')
        print(f'Answer is {a * b}')
        print("------------------------------------------------------------------------------")
        print()
        calculate()

    elif ope == "/":
        print(f'Question ==> {a} {ope} {b} ')
        print(f'Answer is {a / b}')
        print("------------------------------------------------------------------------------")
        print()
        calculate()
        
    elif ope == "esc":
        print(f'Oh Your want to EXIT from here. GOODBYE :-)')
        
    else :
        print(f'Wrong Input {ope}')
        print("------------------------------------------------------------------------------")
        print()
        calculate()


calculate()
