class React:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def display(self):
        print("Area is: ",self.length*self.breadth)
r=React(20,30)
r.display()
r1=React(90,100)
r1.display()