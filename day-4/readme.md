```python
import threading

# Define a BankAccount class to simulate a bank account with deposit and withdrawal methods
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

# Function that simulates a series of account transactions (deposits and withdrawals)
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

```

1. **Importing the threading Module:**
   The code starts by importing the `threading` module, which provides the tools necessary for multi-threading in Python.

2. **BankAccount Class:**
   This class simulates a bank account. It has two main methods: `deposit` and `withdraw`, and it includes a `lock` to ensure thread-safe access to the account balance.

   - **`__init__` Method:** The constructor initializes the account balance to zero and creates a `lock` using `threading.Lock()`.

   - **`deposit` Method:** This method takes an `amount` argument and simulates depositing funds into the account. It uses the `lock` to ensure that only one thread can modify the balance at a time.

   - **`withdraw` Method:** Similar to `deposit`, this method takes an `amount` argument and simulates withdrawing funds from the account while ensuring thread safety.

3. **`account_transactions` Function:**
   This function simulates a series of account transactions, consisting of multiple deposits and withdrawals. It accepts a `BankAccount` instance as an argument.

4. **Main Block:**
   The following steps are executed when the script is run as the main program:

   - An instance of `BankAccount` named `account` is created.

   - Two threads, `thread1` and `thread2`, are created, both targeting the `account_transactions` function and passing the `account` instance as an argument.

   - Both threads are started using the `start()` method, allowing them to run concurrently.

   - The `join()` method is called on both threads to wait for them to finish their transactions before proceeding.

   - Finally, the script prints the final account balance after all transactions.

5. **Thread Safety and Lock Usage:**
   The use of locks (`acquire()` and `release()`) within the `deposit` and `withdraw` methods ensures that only one thread can access and modify the account balance at a time. This prevents data corruption that could occur if multiple threads modify the balance simultaneously.

6. **Concurrent Transactions:**
   The two threads (`thread1` and `thread2`) simulate concurrent account transactions, including deposits and withdrawals. The use of locks ensures that these transactions are performed in a thread-safe manner.

By using locks, the code ensures that the shared resource (the account balance) is accessed in a way that avoids race conditions and maintains data consistency, even in a multi-threaded environment. The example highlights how locks can be used to synchronize access to shared resources, preventing potential issues that arise when multiple threads interact with data concurrently.

---

Steps to run a Python code file named `multithreading_example.py`:

- Open a Terminal (Command Prompt on Windows).

- Navigate to the directory where `multithreading_example.py` is located using the `cd` command.

- Run the script using the `python` command:

  ```
  python multithreading_example.py
  ```

- Observe the output in the Terminal as the script runs.

- Wait for the script to finish executing.

That's it! You've successfully run your `multithreading_example.py` script.