import threading


# Define a BankAccount class to simulate a bank account with deposit and 
# withdrawal methods
class BankAccount:
    def __init__(self):
        # Initialize account balance to zero
        self.balance = 0
        
        # Create a lock to ensure thread-safe access to the balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        """
        Deposit funds into the account.

        Args:
            amount (int): The amount of funds to deposit.
        """
        # Acquire the lock before modifying the balance
        with self.lock:
            print(f"Depositing {amount}")
            self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw funds from the account.

        Args:
            amount (int): The amount of funds to withdraw.
        """
        # Acquire the lock before modifying the balance
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                self.balance -= amount
            else:
                print("Insufficient funds")


# Function that simulates a series of account transactions (deposits\
    # and withdrawals)
def account_transactions(account):
    for _ in range(5):
        account.deposit(100)  # Simulate depositing $100
        account.withdraw(50)   # Simulate withdrawing $50


if __name__ == "__main__":
    # Create a BankAccount instance to work with
    account = BankAccount()
    
    # Create two threads to simulate account transactions
    thread1 = threading.Thread(target=account_transactions, args=(account,))
    thread2 = threading.Thread(target=account_transactions, args=(account,))

    # Start the threads to perform transactions concurrently
    thread1.start()
    thread2.start()

    # Wait for both threads to finish their transactions
    thread1.join()
    thread2.join()

    # Print the final balance after all transactions
    print("Final balance:", account.balance)
