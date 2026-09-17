class glassware:
    def __init__(self, composition):
        self.composition = composition


class beaker(glassware):
    def __init__(self, capacity):
        super().__init__("Glass")
        self.capacity = capacity
   

class Tray:
    def __init__(self):
        self.beakers = [
            beaker(100),
            beaker(100),
            beaker(100),
            beaker(100),
            beaker(100)
        ]
    def display(self):
        print("the tray contains 5 beakers:")
        print() 
        for i, beaker in enumerate(self.beakers, 1):
            print("beaker", i, "has the capacity:", beaker.capacity, "mL and is made with:", beaker.composition)
            print() 


tray = Tray()
tray.display()
del tray
print("the tray has been deleted.")
