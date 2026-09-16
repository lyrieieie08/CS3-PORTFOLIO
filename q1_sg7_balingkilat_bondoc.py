class Glassware:
    def __init__(self, material="Glass"):
        self.material = material
    def display_info(self):
        print(f"Material: {self.material}")


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    def display_info(self):
        print(f"Beaker - Capacity: {self.capacity} mL, Material: {self.material}")


class Tray:
    def __init__(self):
        # Composition: Tray creates and owns 5 Beakers
        self.beakers = [
            Beaker(100),
            Beaker(150),
            Beaker(200),
            Beaker(250),
            Beaker(300)
        ]
    def display_beakers(self):
        print("Tray contains 5 Beakers:")
        for beaker in self.beakers:
            beaker.display_info()


tray = Tray()
tray.display_beakers()
del tray
