def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)
a = int(input("Enter a number: "))
res=factorial(a)
print("Factorial of {} is {}".format(a,res))