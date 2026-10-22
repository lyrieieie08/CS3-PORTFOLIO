class Patient:
    def __init__(self, name: str, bill_amount: float):
        self._name = name
        self._bill_amount = bill_amount
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value: float):
        if value >= 0:
            self._bill_amount = value
        else:
            raise ValueError("Bill amount cannot be negative.")

    def calculate_bill(self) -> float:
        return self._bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self) -> float:
        discount = 0.20
        return self.bill_amount * (1 - discount)

class PhilHealthPatient(Patient):
    def calculate_bill(self) -> float:
        discount = 0.15
        return self.bill_amount * (1 - discount)

if __name__ == "__main__":
    pat1 = Patient("Alice", 1000.0)
    print(f"Patient: {pat1.name}")
    print(f"Original Bill: ₱{pat1.bill_amount:.2f}")
    print(f"Final Bill (Regular): ₱{pat1.calculate_bill():.2f}\n")

    pat2 = SeniorPatient("Bob", 1000.0)
    print(f"Patient: {pat2.name}")
    print(f"Original Bill: ₱{pat2.bill_amount:.2f}")
    print(f"Final Bill (Senior Citizen): ₱{pat2.calculate_bill():.2f}\n")

    pat3 = PhilHealthPatient("Charlie", 1000.0)
    print(f"Patient: {pat3.name}")
    print(f"Original Bill: ₱{pat3.bill_amount:.2f}")
    print(f"Final Bill (PhilHealth): ₱{pat3.calculate_bill():.2f}\n")
