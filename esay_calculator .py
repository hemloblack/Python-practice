def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return ZeroDivisionError
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def calculator(a, b, amal):
    if amal == "+":
        return add(a, b)
    elif amal == "-":
        return subtract(a, b)
    elif amal == "*":
        return multiply(a, b)
    elif amal == "/":
        return divide(a, b)
    elif amal == "^":
        return power(a, b)
    else:
        return "Invalid operator!"
    
a=int(input("enter first number for calculat:\t "))
b=int(input("enter second number for calculat:\t "))
amal=input("enter amalgar for calculat:\t ")

print(calculator(a,b,amal))