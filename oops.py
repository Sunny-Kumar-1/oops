class Employee:
        def __init__(self):
            print("lalalala")
            self.id = 121
            self.salary = 200000
            self.designation = "mlops"
            print("data has been initiated")

        def travel(self,destination):
            print("function is manually initaited")
            print(f"employee to {destination}")
        

sam = Employee()


# sam.travel("goa")

print(type(sam))
