# Day 1: Decorators and Generators
1. Explain the purpose of decorators in Python with an example.
2. Write a decorator that Calculate Total Price Decorator.
3. Write a decorator that authenticate the user username and password.
4. Create a generator function that generates Fibonacci numbers.

Certainly! Here's the formatted code along with instructions for users to copy and execute it:

---
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. The advantage of decorators are

1. **Code Reusability**: Decorators allow you to encapsulate reusable functionality that can be applied to multiple functions. This promotes a DRY (Don't Repeat Yourself) coding philosophy by enabling you to define functionality once and apply it across various parts of your codebase.

2. **Separation of Concerns**: Decorators help separate different concerns within your code. You can keep the core logic of a function focused on its primary task while using decorators to handle cross-cutting concerns like logging, authentication, validation, and more.

3. **Readability**: By abstracting complex functionality into decorators, your main functions become cleaner and more readable. This separation makes the primary purpose of each function clearer and reduces clutter.

4. **Modularity**: Decorators enable you to break down functionality into modular components. This makes your codebase more organized and facilitates changes to individual components without affecting the entire system.

5. **Aspect-Oriented Programming**: Decorators align with the principles of aspect-oriented programming (AOP), which emphasizes separating concerns like logging, security, and performance from the main business logic. This results in more maintainable and adaptable code.

6. **Ease of Maintenance**: Changes or updates to functionality provided by decorators can be applied universally by modifying the decorator code itself. This reduces the need to modify multiple locations in your codebase.

7. **Code Extensibility**: You can easily add new features to existing functions without altering their source code. This is especially useful when you want to augment the behavior of third-party libraries or components.

8. **Testing**: Decorators can simplify unit testing by allowing you to focus on testing the core functionality of functions while mock or test decorators handle additional behavior.

9. **Promoting Best Practices**: Decorators can enforce coding standards and best practices. For instance, you can use a decorator to ensure proper input validation for multiple functions in a consistent manner.

10. **Code Metrics and Profiling**: Decorators can be used to gather metrics, perform profiling, and track performance without affecting the core logic of functions.

11. **Flexible Configuration**: Decorators can accept arguments and provide configuration options, allowing you to customize their behavior for different use cases.

12. **Code Evolution**: As your application evolves, you can modify the behavior of functions by updating or changing decorators. This ensures that changes are applied consistently across the codebase.


---

## Calculate Total Price Decorator

This code demonstrates the use of a decorator function to calculate the total price of two individual prices.

**File: `decorators_1.py`**

```python
# decorators_1.py

def calculate_total_price(func):
    """
    Decorator function to calculate the total price of two individual prices.

    Parameters:
    func (function): The function to be decorated, which should return two \
    individual prices.

    Returns:
    function: Returns a new function that calculates the total price.
    """
    
    def wrapper(*args, **kwargs):
        """
        Inner wrapper function to calculate the total price.
        
        Parameters:
        *args: Arguments from the decorated function.
        **kwargs: Keyword arguments from the decorated function.

        Returns:
        float: Total price calculated by summing two individual prices.
        """
        
        price1, price2 = func(*args)
        return price1 + price2
    
    return wrapper

@calculate_total_price
def calculate_price(*args):
    return args

if __name__ == "__main__":
    price = calculate_price(10, 20)
    print(price)
```

To execute the code:

1. Copy the entire code block above.
2. Create a new file named `decorators_1.py`.
3. Paste the copied code into the `decorators_1.py` file.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the `decorators_1.py` file.
6. Run the command: `python decorators_1.py`

The script defines a decorator `calculate_total_price` that calculates the total price of two individual prices returned by the decorated function. It also provides an example `calculate_price` function that is decorated using `calculate_total_price`. In the example execution block, `calculate_price` is called with individual prices 10 and 20, and the calculated total price is printed.



---
Here's the code description formatted in a similar way for the `decorator_password_matcher.py` file:
## Authenticate User Decorator

This code demonstrates the use of a decorator function to authenticate a user's credentials.

**File: `decorator_password_matcher.py`**

```python
# decorator_password_matcher.py

def authenticate(username, password):
    """
    This function is used to authenticate the user
    Args:
        username (_String_): username of user
        password (_String_): password of user

    Returns:
        _bool_: return `true` if username and password is correct otherwise\
        return false
    """
    return username == "admin" and password == "secret"

def isAuthenticated(func):
    """
    isAuthenticated is used to decorate the authenticate_user 

    Args:
        func (_function_): takes argument as function which is to be decorated
    """
    def wrapper(**kwargs):
        """
        Inner wrapper function to authenticate.
        
        Parameters:
        *args: Arguments from the decorated function.
        **kwargs: Keyword arguments from the decorated function.
        
        """
        username = kwargs["username"]
        password = kwargs["password"]
        if authenticate(username=username, password=password):
            print("Access Granted. Congratulations!")
        else:
            print("Authentication Failed. Access Denied.")
    return wrapper

@isAuthenticated
def authenticate_user(**kwargs):
    return kwargs

if __name__ == "__main__":
    authenticate_user(username="admin", password="secret")
```

To execute the code:

1. Copy the entire code block above.
2. Create a new file named `decorator_password_matcher.py`.
3. Paste the copied code into the `decorator_password_matcher.py` file.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the `decorator_password_matcher.py` file.
6. Run the command: `python decorator_password_matcher.py`

The script defines a decorator `isAuthenticated` that authenticates user credentials. It also provides an example `authenticate_user` function that is decorated using `isAuthenticated`. In the example execution block, `authenticate_user` is called with username "admin" and password "secret" to demonstrate authentication.

---
## Month Names Generator

This Python script generates and prints the names of the months using a generator function.

### Code

The script includes the following components:

```python
# List of month names
months = [
    "January",    # Month index 0
    "February",   # Month index 1
    "March",      # Month index 2
    "April",      # Month index 3
    "May",        # Month index 4
    "June",       # Month index 5
    "July",       # Month index 6
    "August",     # Month index 7
    "September",  # Month index 8
    "October",    # Month index 9
    "November",   # Month index 10
    "December"    # Month index 11
]

def generate_months():
    """
    Generator function to yield month names from the 'months' list.
    
    Yields:
        str: The name of a month.
    """
    for i in months:
        yield i

# Main program
if __name__ == "__main__":
    # Loop through the month names yielded by the generator function
    for months_name in generate_months():
        # Print each month name
        print(months_name)
```
To execute the code:

1. Copy the entire code block above.
2. Create a new file named `month_names_generator.py`.
3. Paste the copied code into the `month_names_generator.py` file.
4. Open a terminal or command prompt.
5. Navigate to the directory containing the `month_names_generator.py` file.
6. Run the command: `python month_names_generator.py`

The script defines a generator function `generate_months()` that yields the names of the months from the predefined list. In the main program section, the generator is used to loop through and print each month name.

### Code Explanation

- `months`: A list of month names with associated indices.
- `generate_months()`: A generator function that yields month names.
- Main program loop that uses the generator to print each month name.

---
## Fibonacci Sequence Generator

This Python script defines a generator function `fibonacci_sequence()` that produces an infinite sequence of Fibonacci numbers.

### Usage

1. Import the `fibonacci_sequence` generator function:

    ```python
    def fibonacci_sequence():
        """
        Generator function to produce Fibonacci sequence.
        
        Yields:
            int: The next number in the Fibonacci sequence.
        """
        a, b = 0, 1  # Initialize the first two Fibonacci numbers
        while True:  # Infinite loop to generate the sequence
            yield a  # Yield the current Fibonacci number
            a, b = b, a + b  # Calculate the next Fibonacci numbers
    ```

2. Create an instance of the generator:

    ```python
    fibonacci_gen = fibonacci_sequence()
    ```

3. Generate and print the first 10 Fibonacci numbers:

    ```python
    for _ in range(10):
        next_fibonacci = next(fibonacci_gen)  # Get the next Fibonacci number
        print(next_fibonacci)  # Print the generated Fibonacci number
    ```

## Fibonacci Sequence Generator

This Python script defines a generator function `fibonacci_sequence()` that produces an infinite sequence of Fibonacci numbers.

### Command to run

1. Make sure you have Python installed on your system.

2. Download the `generator_fibonacci_series.py` script to your local machine.

3. Open a terminal or command prompt and navigate to the directory containing the downloaded script.

4. Run the script using the following command:

    ```bash
    python generator_fibonacci_series.py
    ```






