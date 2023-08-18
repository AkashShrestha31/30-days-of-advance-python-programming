- A context manager in Python efficiently handles resources like files, database connections, and locks, ensuring proper setup and cleanup.
- It simplifies code, prevents resource leaks, and automates resource allocation and deallocation.
- Context managers are crucial when working with resources requiring specific actions before and after use.

### Introduction to Context Managers

- Context managers in Python manage resources systematically, ensuring acquisition and release.
- They work seamlessly with the `with` statement for consistent resource management.
- Context managers help maintain predictability, even in the presence of exceptions.

### Structure of a Context Manager

- Context managers consist of two methods: `__enter__` and `__exit__`.
- `__enter__` initializes resources or performs preparations before code execution.
- `__exit__` cleans up resources, regardless of code block success or exceptions.

### Benefits of Using Context Managers

- Readability and reliability are enhanced by ensuring consistent resource management.
- Context managers prevent common mistakes like resource leaks.
- They simplify coding tasks and promote clean code practices.

Here's the general structure of a context manager:

```bash
class MyContextManager:
    def __enter__(self):
        # Setup resource or perform preparations
        return resource  # Resource to be used in the code block
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Clean up resource, release memory, etc.

# Using the context manager
with MyContextManager() as resource:
    # Code block where the resource is used
    # ...

# Resource is automatically released after the block
```
---

Context managers are widely used in scenarios where you need to ensure proper resource management, such as file handling, database connections, locks, and more. By encapsulating resource setup and cleanup in a context manager, you create more robust and maintainable code.
Here are a few practical use cases where context managers are extremely valuable for properly managing resources in Python:

1. **File Handling:**
   Context managers are commonly used to open and close files, ensuring that files are properly closed after they're used, even if exceptions occur.
   
   ```python
   with open('example.txt', 'r') as file:
       content = file.read()
       print(content)
   ```

2. **Database Connections:**
   When working with databases, context managers can handle the opening and closing of database connections to ensure proper resource management.
   
   ```python
   with db_connection() as connection:
       data = connection.query("SELECT * FROM table")
       # Process data
   ```

3. **Locks and Synchronization:**
   In multi-threaded applications, context managers can help in acquiring and releasing locks or other synchronization mechanisms.
   
   ```python
   with threading.Lock():
       # Critical section of code
   ```

4. **Network Socket Handling:**
   Managing network sockets is crucial for properly releasing resources. Context managers can help handle socket setup and teardown.
   
   ```python
   with open_socket() as socket:
       socket.send(data)
   ```

5. **Resource Cleanup:**
   Context managers are useful for resource cleanup tasks like releasing memory, closing connections, and more.
   
   ```python
   with resource_manager() as resource:
       # Use the resource
   ```

6. **Custom Resource Management:**
   You can create custom context managers for any scenario where you need to ensure resource setup and cleanup.
   
   ```python
   with custom_resource_manager() as resource:
       # Use the resource
   ```

In all these scenarios, context managers help ensure that resources are acquired when needed and properly released when they're no longer needed, preventing resource leaks and improving the overall reliability of your code.

---

 Here's the complete code for `file_content_manager.py` script, including the `File` class and the README instructions:

**file_content_manager.py:**
```python
class File:
    """
    A context manager for file handling.

    Args:
        filename (str): The name of the file to work with.
        mode (str, optional): The mode in which to open the file (default is 'r').

    Usage:
        with File("user.csv") as file:
            content = file.read()
            print(content)
    """

    def __init__(self, filename, mode='r'):
        """
        Initialize the File context manager.

        Args:
            filename (str): The name of the file.
            mode (str, optional): The mode in which to open the file (default is 'r').
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Enter the context and open the file.

        Returns:
            _io.TextIOWrapper: The file object.
        """
        print(f"Opening file {self.filename} in '{self.mode}' mode...")
        print("--------------------------------------------------------")
        self.file = open(self.filename, self.mode, encoding='utf-8',
                         errors='ignore')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context and close the file.

        Args:
            exc_type: The exception type (if any).
            exc_val: The exception value (if any).
            exc_tb: The exception traceback (if any).
        """
        if self.file:
            self.file.close()
            print(f"Closing file {self.filename}...")


if __name__ == "__main__":
    try:
        with File("information.csv") as file:
            content = file.read()
            print(content)
            print("--------------------------------------------------------")
    except FileNotFoundError as e:
        print(f"The exception is {e}")
```

# File Content Manager

The `File` class is a custom context manager designed to handle file operations. It allows you to open and work with files within a context, ensuring proper resource management.

## Usage

1. **Import the `File` class:**

    ```python
    from file_content_manager import File
    ```

2. **Create an instance of `File` within a `with` block:** 

    ```python
    try:
        with File("information.csv") as file:
            content = file.read()
            print(content)
            print("--------------------------------------------------------")
    except FileNotFoundError as e:
        print(f"The exception is {e}")
    ```

The class takes care of opening and closing the file while you work with it, ensuring resource cleanup even in the presence of exceptions.

## Running the Script

To run the script, follow these steps:

1. Save the code in a file named `file_content_manager.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `file_content_manager.py` is located.
4. Run the script using the command:

   ```
   python file_content_manager.py
   ```
---

## Custom Context Manager Example

The provided code demonstrates the creation and usage of a custom context manager using the `contextlib` module. The custom context manager allows you to open files within a context, automatically handling file opening and closing.

### Code Explanation

```python
from contextlib import contextmanager

@contextmanager
def custom_context_manager(filename, mode='r'):
    """
    A custom context manager for file handling.

    Args:
        filename (str): The name of the file to open.
        mode (str, optional): The mode in which to open the file (default is 'r').

    Yields:
        _io.TextIOWrapper: The file object.

    Usage:
        with custom_context_manager("information.csv") as file:
            content = file.read()
            # Process content
    """
    file = None
    try:
        print(f"Opening File: {filename}")
        print("--------------------------------------------------------")
        file = open(filename, mode=mode, encoding='utf-8', errors='ignore')
        yield file
    finally:
        if file:
            file.close()
            print(f"Closing File: {filename}")
```

###Instructions

1. **Run the script:** Save the code in a file named `contextlib_custom_context_manager.py`. Open a terminal or command prompt and navigate to the directory where `contextlib_custom_context_manager.py` is located. Run the script using the command:

   ```
   python contextlib_custom_context_manager.py
   ```

2. **Using the custom context manager:** The script defines a custom context manager named `custom_context_manager` that allows you to open a file within a context. The usage is as follows:

   ```python
   from contextlib_custom_context_manager import custom_context_manager

   try:
       with custom_context_manager("information.csv") as file:
           content = file.read()
           # Process content
   except FileNotFoundError as e:
       print(f"Exception: {e}")
   ```

   The custom context manager takes care of opening and closing the file, ensuring proper resource management even in the presence of exceptions.

---

By using context managers, like the custom one demonstrated above, you can streamline resource management and ensure clean and reliable code execution.

---

## Efficient File Reading using Custom Context Manager

The `problem1.py` script demonstrates the use of a custom context manager for reading files line by line without loading the entire content into memory.

### Code Explanation

```python
from contextlib import contextmanager

@contextmanager
def read_file(filename, mode='r'):
    """
    A custom context manager for reading files line by line without loading the entire file into memory.

    Args:
        filename (str): The name of the file to read.
        mode (str, optional): The mode in which to open the file (default is 'r').

    Yields:
        _io.TextIOWrapper: The file object.

    Usage:
        with read_file("information.csv") as file:
            for line in file:
                print(line, end='')
    """
    try:
        with open(filename, mode=mode, encoding='utf-8', errors='ignore') as file:
            yield file  # The file is automatically closed when exiting the context
    finally:
        pass  # No need to close the file explicitly, the 'with' statement handles it


if __name__ == "__main__":
    try:
        with read_file("information.csv") as file:
            for line in file:
                print(line, end='')

    except FileNotFoundError as e:
        print(f"Exception: {e}")
```

### Usage

1. **Save the script:** Copy the code above and save it in a file named `problem1.py`.

2. **Run the script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `problem1.py` is located.
   - Run the script using the command:
     ```
     python problem1.py
     ```

### Example Usage

```python
from problem1 import read_file

# Using the custom context manager
try:
    with read_file("information.csv") as file:
        for line in file:
            print(line, end='')
except FileNotFoundError as e:
    print(f"Exception: {e}")
```

- The `with` statement ensures proper file handling, including automatic closure.
- The custom context manager enables efficient line-by-line reading of large files.


---
