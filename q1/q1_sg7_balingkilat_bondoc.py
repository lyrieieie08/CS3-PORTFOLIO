class Glassware:
    def __init__(self, composition="Glass"):
        self.composition = composition
    def display_info(self):
        print(f"Composition: {self.composition}")


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    def display_info(self):
        print(f"Beaker - Capacity: {self.capacity} mL, Composition: {self.composition}")


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(100),
            Beaker(100),
            Beaker(100),
            Beaker(100),
            Beaker(100)
        ]
    def display_beakers(self):
        print("Tray contains 5 Beakers:")
        for beaker in self.beakers:
            beaker.display_info()


tray = Tray()
tray.display_beakers()
del tray
