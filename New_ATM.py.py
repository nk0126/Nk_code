class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello, welcome 
1. Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit
""")
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Thank you for using our service. Goodbye!")
                break
            else:
                print("Invalid input, please try again.")

    def create_pin(self):
        self.pin = input("Create your new pin: ")
        print("Pin created successfully!")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self.balance}")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

# Create an instance of the Atm class to run the program
atm = Atm()
