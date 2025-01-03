import time

print("Please insert yout Card")

time.sleep(5)

password = 1234

balance = 5000
while True:
    pin = int(input("Enter your ATM PIN: "))
    if pin != password:
        print("Wrong PIN. Please try again.")

    else:
        while True:
            try:
                print(
                        """
                        1. Balance
                        2. Withdraw balance
                        3. Deposit balance
                        4. Exit
                        """
                    )
                option = int(input("Please enter your choice: "))
            except:
                print("Invalid option. Please enter a number.")
            
            if option == 1:
                print("Your current balance is:", balance)
            elif option == 2:
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= withdraw_amount
                    print(withdraw_amount,"is debited from your account.")
                    print("Your new balance is:", balance)
            elif option == 3:
                deposit_amount = int(input("Enter the amount to deposit: "))
                balance += deposit_amount
                print(deposit_amount,"is credited to your account.")
                print("Your new balance is:", balance)
            elif option == 4:
                print("Thank you for using our ATM. Goodbye!")
                exit()
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
# Alternatively, you can use the advanced version of the ATM Machine Simulation which is based on the built-in functions.

'''

import time

def display_menu():
    print(
        """
        1. Balance
        2. Withdraw balance
        3. Deposit balance
        4. Exit
        """
    )

def check_pin(password):
    attempts = 3
    while attempts > 0:
        try:
            pin = int(input("Enter your ATM PIN: "))
            if pin == password:
                return True
            else:
                attempts -= 1
                print(f"Wrong PIN. You have {attempts} attempts left.")
        except ValueError:
            print("Invalid input. Please enter a numeric PIN.")
    return False

def main():
    print("Please insert your Card")
    time.sleep(2)

    password = 1234
    balance = 5000

    if not check_pin(password):
        print("Too many incorrect attempts. Exiting.")
        return

    while True:
        display_menu()
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if option == 1:
            print("Your current balance is:", balance)
        elif option == 2:
            try:
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                else:
                    balance -= withdraw_amount
                    print(withdraw_amount, "is debited from your account.")
                    print("Your new balance is:", balance)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif option == 3:
            try:
                deposit_amount = int(input("Enter the amount to deposit: "))
                balance += deposit_amount
                print(deposit_amount, "is credited to your account.")
                print("Your new balance is:", balance)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif option == 4:
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid choice.")

if __name__ == "__main__":
    main()

'''