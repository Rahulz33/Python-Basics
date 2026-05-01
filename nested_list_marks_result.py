names=["Raju","Dhoni","Virat","Rohit","Hardik"]
marks=[[20,30,40],[30,40,50],[40,50,60],[50,60,70],[60,70,80]]
for i in range(5):
    a=sum(marks[i])//3
    print("{}. {} has scored {}".format(i+1,names[i],a))