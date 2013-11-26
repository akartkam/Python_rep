class Parent():
    def setdata(self, data):
        self.data = data

    def show(self):
        print(self.data)

    def __add__(self, other):
        return self.data + " " + other.data

class Childe(Parent):
    def show(self):
        print(self.data + "| from Childe")
    

myexp1 = Parent()
myexp2 = Childe()

myexp1.setdata("My first obj")
myexp2.setdata("My second obj")

myexp1.show()
myexp2.show()

print(myexp1 + myexp2)


