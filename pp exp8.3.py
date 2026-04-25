class BillSplit:
    def divide_bill(self, bill, people):
        if people == 0:
            print("Error: Cannot divide bill among zero people!")
        else:
            print("Each person pays:", bill / people)


b = BillSplit()
b.divide_bill(1000, 5)
b.divide_bill(1000, 0)