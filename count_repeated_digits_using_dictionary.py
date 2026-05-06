a=int(input("Enter any number:  "))
b = {}
for i in str(a):
    if i in b:
        b[i] = b[i] + 1
    else:
        b[i] = 1
d=[i[1] for i in b.items() if i[1]>1]
print(len(d))