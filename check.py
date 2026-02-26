#list based transation system
balance = 80
transactions = []
while True:
    print("\nCurrent Balance: ", balance)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Transactions")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: {amount}")
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '2':
        amount = int(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew: {amount}")
            print(f"{amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    
    elif choice == '3':
        print("\nTransaction History:")
        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions yet.")
    
    elif choice == '4':
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")