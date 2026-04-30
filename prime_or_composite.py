a=int(input("Enter any number: "))
c=0
for i in range(2,a):
    if a%i==0:
        c=c+1
if c==0:
    print(f"{a} is a prime number")
else:
    print(f"{a} is a composite number")
