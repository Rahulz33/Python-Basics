print("Enter value of a: ")
a = int(input())
print("Enter value of b: ")
b = int(input())
print("Enter value of c: ")
c = int(input())
if a > b and a > c:
    if b>c:
        print("second greatest is b")
    else:
        print("second greatest is c")
elif b > a and b > c:
    if a>c:
        print("second greatest is a")
    else:
        print("second greatest is c")
else:
    if a>b:
        print("second greatest is a")
    else:
        print("second greatest is b")
