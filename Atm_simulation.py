# Simple ATM Simulation

# Initial balance and PIN
balance = 1000
correct_pin = "1234"

# ----------- LOGIN SYSTEM -----------
pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Incorrect PIN. Access Denied.")
else:
    print("Login Successful!")

    # ----------- ATM MENU LOOP -----------
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # ----------- CHECK BALANCE -----------
        if choice == "1":
            print(f"Your current balance is: ₹{balance}")

        # ----------- DEPOSIT MONEY -----------
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid amount!")

        # ----------- WITHDRAW MONEY -----------
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= balance and amount > 0:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount!")

        # ----------- EXIT -----------
        elif choice == "4":
            print("Thank you for using owr ATM Service. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")