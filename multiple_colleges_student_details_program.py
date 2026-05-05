country = "india"
class ace:
    clg = "ACE College"
    def give_details(self, l, b, h, r):
        self.tot = l + b + h
        self.name = r

    def display(self):
        print("1. Name : ", self.name)
        print("2. Total Marks : ", self.tot)
        print("3. College : ", ace.clg)
        print("4. Country : ", country)
        print()

class bvrit:
    clg = "BVRIT College"
    def give_details(self, a, c, d, e):
        self.tot = a + c + d
        self.name = e

    def display(self):
        print("1. Name : ", self.name)
        print("2. Total Marks : ", self.tot)
        print("3. College : ", bvrit.clg)
        print("4. Country : ", country)
        print()

a = ace()
b = bvrit()
a2 = ace()
b2 = bvrit()
a.give_details(20,30,40,"Rahul")
b.give_details(25,35,45,"Avinash")
a2.give_details(30,40,50,"Bhushan")
b2.give_details(35,45,55,"Doper")
a.display()
b.display()
a2.display()
b2.display()