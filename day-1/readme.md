# Day 1: Decorators and Generators
1. Explain the purpose of decorators in Python with an example.
2. Write a decorator that measures the time taken by a function to 
execute.
3. Create a generator function that generates Fibonacci numbers.

Certainly! Here's the formatted code along with instructions for users to copy and execute it:

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

Users can follow the provided instructions to create the file, paste the code, and execute it to see the decorator in action.

I understand. Here's the code description formatted in a similar way for the `decorator_password_matcher.py` file:

---

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

Users can follow the provided instructions to create the file, paste the code, and execute it to see the decorator in action.