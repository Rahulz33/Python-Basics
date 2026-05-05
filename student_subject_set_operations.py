maths=["Avinash","Bhushan","Rahul","Doper","Emmanuel"]
social=["Rahul","Avinash","Nupur","Shreya","Esha"]
computer=["Rahul","Bhushan","Shreya","Avinash","Nupur"]

m=set(maths)
s=set(social)
c=set(computer)

a=m|s|c
print("Students who are in atleast one subject : ",list(a))

x=(m&s)|(s&c)|(m&c)
print("Students who are in atleast two subjects : ",list(x-(m&s&c)))

print("Students who passed in three subjects : ",list(m&s&c))