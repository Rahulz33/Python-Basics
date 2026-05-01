names=["Raju","Dhoni","Virat","Rohit","Hardik"]
marks=[45,30,78,23,90]
p=1
for i in range(5):
    if marks[i]> 40:
        print("{}. {} has scored {}%".format(p,names[i],marks[i]))
        p=p+1