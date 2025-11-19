def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
try:
    number=int(input("enter a non-negative integer to calculate its factorial"))
    if number<0:
        print("invalid input,please enter a non-negative integer")
    else:
        print(factorial(number))
except:
    print("invalid")