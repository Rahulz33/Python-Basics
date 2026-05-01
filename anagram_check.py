a=input("Enter string 1: ")
b=input("Enter string 2: ")

a1="".join(i.lower() for i in a if i.isalnum())
b1="".join(i.lower() for i in b if i.isalnum())

a2=sorted(a1)
b2=sorted(b1)

if a2==b2:
    print("The given strings are anagrams")
else:
    print("The given strings are not anagrams")