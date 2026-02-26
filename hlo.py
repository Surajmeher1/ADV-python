# Basic Transaction System (List Based)

balance = 0
transactions = []
password = "suraj123"


def validate_password(p):
    return p == password


def take_password():
    return input("Enter Password: ")


def deposit():
    global balance
    amt = int(input("Enter Deposit Amount: "))
    balance += amt
    transactions.append(f"Deposit : {amt}")
    print(" Amount Deposited Successfully")


def withdraw():
    global balance
    amt = int(input("Enter Withdraw Amount: "))

    if amt > balance:
        print(" Insufficient Balance! Deposit first.")
    else:
        balance -= amt
        transactions.append(f"Withdraw : {amt}")
        print("Amount Withdrawn Successfully")


def show_balance():
    print(f" Current Balance: {balance}")


def show_transactions():
    print("\n Transaction History")
    if len(transactions) == 0:
        print("No Transactions Found")
    else:
        for t in transactions:
            print("-", t)


def menu():
    print("\n========== BANK MENU ==========")
    print("0. Reset Password")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    print("================================")



while True:
    input_pass = take_password()

    if validate_password(input_pass):
        print("\n Login Successful! Welcome!")

        while True:
            menu()
            choice = int(input("Enter Your Choice: "))

            if choice == 0:
                password = take_password()
                print("Password Reset Successfully")
                break  # logout after reset password

            elif choice == 1:
                deposit()

            elif choice == 2:
                withdraw()

            elif choice == 3:
                show_balance()

            elif choice == 4:
                show_transactions()

            elif choice == 5:
                print(" Thanks for using the system!")
                exit()

            else:
                print(" Invalid Choice! Try Again")

    else:
        print(" Wrong Password! Try Again.\n")
