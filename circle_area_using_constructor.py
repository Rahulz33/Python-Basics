class CIRCLE:
    def __init__(self):
        x=int(input("Enter the radius of the circle: "))
        self.radius = x
    def area(self):
        print("Area of the circle is: ",3.14*self.radius**2)

a=int(input("Enter the number of circles: "))
circles = []
for i in range(a):
    c=CIRCLE()
    circles.append(c)
    c.area()
    print("________________________________________")