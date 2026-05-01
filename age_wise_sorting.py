names=["raju","dhoni","virat","rohit","hardik"]
age=[30,20,40,50,60]
res=list(zip(age,names))
res1=sorted(res,reverse=True)
p=1
for i in res1:
    print("{}. {} age is {}".format(p,i[1],i[0]))
    p=p+1