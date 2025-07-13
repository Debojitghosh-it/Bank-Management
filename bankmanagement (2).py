

import json
import os

DATA_FILE = "bank_data.json"

# Load accounts data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save accounts data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Create a new account
def create_account():
    accounts = load_data()
    acc_num = input("Enter new account number: ")
    if acc_num in accounts:
        print("Account already exists.")
        return
    name = input("Enter account holder name: ")
    accounts[acc_num] = {"name": name, "balance": 0}
    save_data(accounts)
    print("Account created successfully!")

# Deposit money
def deposit():
    accounts = load_data()
    acc_num = input("Enter account number: ")
    if acc_num not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount.")
        return
    accounts[acc_num]["balance"] += amount
    save_data(accounts)
    print(f"Deposited ₹{amount} successfully!")

# Withdraw money
def withdraw():
    accounts = load_data()
    acc_num = input("Enter account number: ")
    if acc_num not in accounts:
        print("Account not found.")
        return
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
        return
    if accounts[acc_num]["balance"] < amount:
        print("Insufficient balance.")
        return
    accounts[acc_num]["balance"] -= amount
    save_data(accounts)
    print(f"Withdrew ₹{amount} successfully!")

# Check balance
def check_balance():
    accounts = load_data()
    acc_num = input("Enter account number: ")
    if acc_num not in accounts:
        print("Account not found.")
        return
    balance = accounts[acc_num]["balance"]
    name = accounts[acc_num]["name"]
    print(f"Account Holder: {name}\nBalance: ₹{balance}")

# Delete account
def delete_account():
    accounts = load_data()
    acc_num = input("Enter account number to delete: ")
    if acc_num not in accounts:
        print("Account not found.")
        return
    confirm = input("Are you sure you want to delete this account? (yes/no): ")
    if confirm.lower() == "yes":
        del accounts[acc_num]
        save_data(accounts)
        print("Account deleted successfully.")
    else:
        print("Deletion cancelled.")

# Main menu
def main():
    while True:
        print("\n====== Bank Management System ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

