import random

# Class representing a User
class User:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.activity_history = []

    def deposit(self, amount):
        self.balance += amount
        self.activity_history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.activity_history.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient funds!")

# Collection of ads
ads = [
    "Ad 1: Enjoy our premium banking services!",
    "Ad 2: Save more with our high interest rates!",
    "Ad 3: Join us for a secure and convenient banking experience!"
]

# Function to display a random ad
def display_ad():
    random_ad = random.choice(ads)
    print(random_ad)

# Function for user login
def login():
    username = input("Username: ")
    password = input("Password: ")

    # Perform user authentication
    if username == "your_username" and password == "your_password":
        return User(username, password)
    else:
        return None

# Main program
def main():
    display_ad()
    user = login()

    if user:
        print("Login successful!")
        while True:
            print(f"Balance: {user.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter the deposit amount: "))
                user.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: "))
                user.withdraw(amount)
            elif choice == "3":
                break
            else:
                print("Invalid choice!")

    else:
        print("Invalid credentials. Login failed.")

if __name__ == "__main__":
    main()
