class Registration:
    def register(self, name, age):
        if age <= 0 or age > 120:
            print("Invalid age! Please enter a valid age.")
        else:
            print("Registration successful for", name)


user = Registration()
user.register("Rahul", 25)
user.register("Amit", -5)