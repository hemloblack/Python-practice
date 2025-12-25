def divide(a, b):
    return a / b


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = divide(num1, num2)
        print("Result:", result)
        break  
    except ZeroDivisionError:
        print("خطا: تقسیم بر صفر مجاز نیست.")
    except ValueError :
        print("خطا: لطفاً فقط عدد صحیح وارد کنید.")

    
