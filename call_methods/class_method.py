class employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

print(employee.raise_amount)

employee.set_raise_amt(20)
print(employee.raise_amount)