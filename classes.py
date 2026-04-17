class person:
    def __init__(self, name,age,email,address,dob):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.dob = dob 

    def talk(self):
        print(f"{self.name} talks") 
      

person1 = person("abdi",24,"aabdi@gmail.comm","karen","2001-04-13")
print(type(person1))
print(person1.address)
person1.talk()


person2 = person("khalid",24,"khalid@gmail.comm","eastleigh","2003-04-23")
print(type(person2))
print(person2.address)
person2.talk()




class BankAccount:
    # 1. Create the class with required attributes
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount): self.balance -= amount
    def display_info(self): 
     print(f"Owner: {self.owner_name} | Acc: {self.account_number} | Balance: {self.balance}")

# 1. create two bankaccount objects
account1 = BankAccount("001", 100, "abdi", "Apr-16")
account2 = BankAccount("002", 500, "khalid", "Apr-16")

# 2. test the methods
account1.deposit(50)
account1.withdraw(20)
account1.display_info()

account2.deposit(100)
account2.withdraw(200)
account2.display_info()



class Car:
    def __init__(self, brand, model, year, fuel_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0  # Starts empty
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"The {self.brand} is now running.")
        else:
            print("Cannot start: The tank is empty!")

    def stop(self):
        self.is_running = False
        print(f"The {self.brand} engine is off.")

    def refuel(self, liters):
        if self.fuel_level + liters <= self.fuel_capacity:
            self.fuel_level += liters
            print(f"Added {liters}L. Current fuel: {self.fuel_level}L")
        else:
            self.fuel_level = self.fuel_capacity
            print(f"Tank is full at {self.fuel_capacity}L.")

    def drive(self):
        if not self.is_running:
            print("Start the car first!")
        elif self.fuel_level <= 0:
            print("Out of fuel!")
            self.stop()
        else:
            self.fuel_level -= 2 # Each drive consumes 2L
            print(f"Driving... fuel level is now {self.fuel_level}L.")

    def display_car_info(self):
        print("Car Details")
        print(f"Vehicle: {self.year} {self.brand} {self.model}")
        print(f"Fuel Status: {self.fuel_level}/{self.fuel_capacity}L")
        print(f"Engine Running: {self.is_running}")
        

# Testing the implementation 
my_car = Car("Toyota", "Axio", 2023, 50)
my_car.display_car_info()
my_car.refuel(30)
my_car.start()
my_car.stop()
my_car.drive()
my_car.display_car_info()