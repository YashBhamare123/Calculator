# Defining the value of pi and e for further use in text replacement
pi = 3.1415926535
e = 2.7182818284
# Initializing the variables present in code without giving them any value
n1 = None
n2 = None
n3 = None
n4 = None
ans = None
root1 = None
root2 = None

# Explaining the rules and syntax
# Providing the list of operations available for use and the way to access them
# Also explaining how to use the answer obtained just before
print("""\033[4m\033[1mWelcome to PyCalc\033[0m\033[0m:\nHere is the list of available operations\n
'+': add
'-': subtract
'*': multiply
'/': divide
'log': log
'sin': sin
'cos': cos
'tan': tan
'cot': cot
'sec': sec
'cosec': cosec
'exp': exponential
'qd': quadratic_eq
'le': linear equations

Type the word in 'single quotes' to use that operation
Eg : \033[3mPick an operation to perform
     sin\033[0m 
     
If you want to use special numbers, type \033[1m'pi'\033[0m for the value of pi and and \033[1m'e'\033[0m for the value of euler's number

NOTE: To use the answer obtained in the previous calculation, type \033[1m'ans'\033[0m in the field where it asks for the 
      value of Eg. Base or Number 1. The answer obtained in the previous calculation will be substituted in its place
       \033[3m(this functionality is not available for answers that have been obtained by quadratic equations)\033[0m
       
       For \033[1msquare roots, cube roots, etc, give decimal input in the exponent field of the exponential function\033[0m\n

Some Limitations: 1. Due to the algorithm used for calculating sec and cosec functions, there might be an error in calculations
                  near the input where function is Not Defined or tends to Infinity.
                  2. After using the quadratic function, the process to allow calculating is not currently available.
                  Please copy and paste the values of the desired roots in the appropriate fields. Inconvenience is 
                  regretted""")



# Defining the addition function
def add(n1, n2):
    n1 = input("Enter the first number\n").strip()
    n2 = input("Enter the second number\n").strip()
    # Text replacement for some commonly used values
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n2 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
    n1 = float(n1)
    n2 = float(n2)
    return n1 + n2


# Defining the subtract function
def subtract(n1, n2):
    n1 = input("Enter the first number\n").strip()
    n2 = input("Enter the second number\n").strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n2 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
    n1 = float(n1)
    n2 = float(n2)
    return n1 - n2


# Defining the multiplication function
def multiply(n1, n2):
    n1 = input("Enter the first number\n").strip()
    n2 = input("Enter the second number\n").strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n2 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
    n1 = float(n1)
    n2 = float(n2)
    return n1 * n2


# Defining the division function
def divide(n1,n2):
    n1 = input("Enter the Dividend (Numerator)\n").strip()
    n2 = input("Enter the Divisor (Denominator)\n").strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n1 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
        n1 = ans
    n1 = float(n1)
    n2 = float(n2)
    if n2 != 0:
        return n1/n2
    else:
        return "Divide by zero error"


# Defining the log function
# Algorithm used for this function gives answers accurate till infinite decimal places
def log(n1, n2):
    n1 = (input("Enter the argument\n")).strip()
    n2 = (input("Enter the base\n")).strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n2 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
    n1 = float(n1)
    n2 = float(n2)
    n = 1
    # Finding the closest power of base to argument
    for i in range(int(n1)):
        if n1 >= n2 ** i:
            n = i
        else:
            break
    # Concatenating that value as a number with a decimal point next to it
    log_val = f"{n}."
    # Dividing the closest base power and raising the power to 10 to find the next closest power for our first decimal place
    # Eg. 42 = 10^(1.xyz...) where 1. was determined from the first step
    # 4.2 = 10^(0.xyz)
    # 4.2^(10) = 10^(x.yz)
    # now we can find the closest power of 10 to LHS and that will be x
    ph = (n1 / n2 ** n) ** 10
    # Looping the above explained algorithm 10 times to get 10 decimal place accuracy
    for x in range(10): #change this range to vary the accuracy
                        #3 = 3 decimal places, 10 = 10 decimal places

        for i in range(int(ph)):
            if ph >= n2 ** i:
                n = i
            else:
                break
        log_val = log_val + f"{n}"
        ph = (ph / (n2 ** n)) ** 10
    if n1 != 0 and n2 != 0:
        return float(log_val)
    else:
        return "Base or Argument zero"


# Defining the Factorial Function (not for user's use but rather for Taylor Series Expansion)
def factorial(n1):
    fact = n1
    multiplier = n1
    if n1 == int(n1) and n1 > 0:
        while multiplier > 1:
            multiplier -= 1
            fact = fact * multiplier
        return fact
    elif n1 == 0:
        return 1


# Defining sin function using Taylor Series Expansion
def sin(n1):
    n1 = (input("Enter the value in radians\n")).strip()
    if n1 == 'ans':
        n1 = ans
    elif n1 == 'e':
        n1 = e
    elif n1 == 'pi':
        n1 = pi
    else:
        n1 = float(n1)
    y = 0
    # Because only 50 terms exist in Taylor Expansion Defined below, Larger numbers do not converge
    # They require more than 50 terms to converge accurately and if used without modifications, the function gives absurd values
    # Thus the below loop is written to find any large number's equivalent, in a smaller domain to give the correct result
    while not 0 <= n1 < 2 * pi:
        n1 = n1 - 2 * pi
    # Range here is set 50 because Python gives 'number too large to be stored error' after a certain point
    for i in range(50):
        y = y + (n1 ** (2 * i + 1)) / (factorial(2 * i + 1)) * (-1) ** i
    return y


# Defining Cos function using Taylor Series Expansion
def cos(n1):
    n1 = (input("Enter the value in radians\n")).strip()
    if n1 == 'ans':
        n1 = ans
    elif n1 == 'e':
        n1 = e
    elif n1 == 'pi':
        n1 = pi
    else:
        n1 = float(n1)
    y=0
    while not 0 <= n1 < 2 * pi:
        n1 = n1 - 2 * pi
    for i in range(50):
        y = y + ((n1) ** (2 * i)) / (factorial(2 * i)) * (-1) ** i
    return y


# Defining tan function using Taylor Series Expansion
def tan(n1):
    n1 = (input("Enter the value in radians\n")).strip()
    if n1 == 'ans':
        n1 = ans
    elif n1 == 'e':
        n1 = e
    elif n1 == 'pi':
        n1 = pi
    else:
        n1 = float(n1)
    y = 0
    x = 0
    while not 0 <= n1 < 2 * pi:
        n1 = n1 - 2 * pi
    for i in range(50):
        # x and y used to store value of sin and cos to make sure that the input of n1(included in sin and cos function)
        # is not taken twice
        x = x + (n1 ** (2 * i)) / (factorial(2 * i)) * (-1) ** i
        y = y + (n1 ** (2 * i + 1)) / (factorial(2 * i + 1)) * (-1) ** i
    # 22273401082.786457 is used in the check for infinity because that is the largest value that can be obtained by this 50 term Taylor Series Aproximation
    if x != 0:
        return y/x
    else:
        return "Infinity"


# Defining cot function as the reciprocal of tan
def cot(n1):
    # tan_value variable used to avoid calling tan function again (taking input again) in the if statement check for a zero
    tan_value = tan(n1)
    if tan_value != 0:
        return 1/tan_value
    else:
        return "Infinity"


# Defining sec function as the reciprocal of cos
def sec(n1):
    cos_value = cos(n1)
    if cos_value != 0:
        return 1/(cos_value)
    else:
        return "Infinity"


# Defining cosec function as the reciprocal of sin
def cosec(n1):
    sin_value = sin(n1)
    if sin_value != 0:
        return 1/sin_value
    else:
        return "Infinity"


# Defining exponential function using the built-in '**' notation
def exponential(n1,n2):
    n1 = (input("Enter the base\n")).strip()
    n2 = (input("Enter the exponent\n")).strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'pi':
        n2 = pi
    elif n2 == 'e':
        n2 = e
    if n1 == "ans":
        n1 = ans
    elif n1 == 'pi':
        n1 = pi
    elif n1 == 'e':
        n1 = e
    n1 = float(n1)
    n2 = float(n2)
    return n1**n2


# Defining the Quadratic Function
def quadratic_eq(n4, n2, n3):
    print("ax\u00b2 + bx + c = 0")
    n4 = input("a= ").strip()
    n2 = input("b= ").strip()
    n3 = input("c= ").strip()
    if n2 == "ans":
        n2 = ans
    elif n2 == 'e':
        n2 = e
    elif n2 == 'pi':
        n2 = pi
    if n4 == "ans":
        n4 = ans
    elif n4 == 'e':
        n4 = e
    elif n4 == 'pi':
        n4 = pi
    if n3 == "ans":
        n3 = ans
    elif n3 == 'e':
        n3 = e
    elif n3 == 'pi':
        n3 = pi
    n4 = float(n4)
    n2 = float(n2)
    n3 = float(n3)
    # Initialization
    root1=None
    root2=None
    # Checking for the nature of roots
    if n4 == 0:
        return "Not a quadratic equation. Please use the linear equation function"
    elif n2**2 < 4*n4*n3:
        return "Function has Complex Roots"
    elif n4 == 0:
        return "Not a quadratic equation. Please use the linear equation function"
    elif n2**2 >= 4*n4*n3:
        root1 = (-n2 + (n2**2 - 4*n4*n3)**(1/2))/(2*n4)
        root2 = (-n2 - (n2**2 - 4*n4*n3)**(1/2))/(2*n4)
        # returning the value in the form of a string
        return f"Root 1 = {root1}\nRoot 2 = {root2}"


# Defining Linear Equation function
def linear_equations(n1, n2, n3):
    print("ax + b = c ")
    n1 = input("a= ").strip()
    n2 = input("b= ").strip()
    n3 = input("c= ").strip()
    if n2 == "ans":
        n2 = ans
    if n1 == "ans":
        n1 = ans
    if n3 == "ans":
        n3 = ans
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    # Checking for coeff of x to avoid divided by zero error
    if n1 != 0:
        return (n3-n2)/n1
    if n1 == 0:
        return "Not a linear equation"


# listing operations in a dictionary to call them using the entered key
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'log': log,
    'sin': sin,
    'cos': cos,
    'tan': tan,
    "cot": cot,
    "sec": sec,
    "cosec": cosec,
    "exp": exponential,
    'qd': quadratic_eq,
    'le': linear_equations
}

# Loop to continue calculating with the obtained result
continue_calc = "yes"
while continue_calc == 'yes':
    op = input("Pick an operation to perform:\n").strip()
    # separating functions by no.of parameters so that they can be called using the appropriate parameters
    if op in {'+', '-', '*', '/', 'exp', 'log'}:
        ans = operations[op](n1,n2)
    elif op in {'sin', 'cos', 'tan', 'cot', 'sec', 'cosec'}:
        ans = operations[op](n1)
    elif op == 'le':
        ans = operations[op](n1, n2, n3)

    # Checking if the returned value is string or not, so that rounding off can be done without altering the actual ans
    if op != 'qd' and not isinstance(ans, str):
        ans_round = round(ans, 7)
        print(f"\n\033[1m{ans_round}\033[0m")
    # Using condition to print the return type
    elif op != 'qd' and isinstance(ans, str):
        print(ans)
    else:
        print(quadratic_eq(n4, n2, n3))

    # Separating the string type returns because they correspond to error in evaluation
    # We need to stop the loop if ans is string, as answer won't be a float, thus no further calculation can be done
    if isinstance(ans, str):
        continue_calc = 'no'
    else:
        continue_calc = (input("Do you want to continue calculating with this result, 'yes' or 'no' ").lower()).strip()
