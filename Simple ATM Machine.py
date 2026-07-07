#Simple ATM Machine
pin = "2444"
balance = 5000

user_pin = input("Enter PIN: ")

if user_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            print("Balance =", balance)
        elif choice == 2:
            amount = int(input("Enter Amount: "))
            balance += amount
            print("Amount Deposited")
        elif choice == 3:
            amount = int(input("Enter Amount: "))
            if amount <= balance:
                balance -= amount
                print("Amount Withdrawn")
            else:
                print("Insufficient Balance")
        elif choice == 4:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")
else:
    print("Wrong PIN")