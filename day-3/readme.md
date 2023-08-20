# Day 3: Metaclasses and Reflection
1. Explain what metaclasses are and how they are used in Python.
2. Write a metaclass that automatically converts all attribute names to 
uppercase.
3. How can you access the list of attributes and methods of an object using 
reflection?

---

A metaclass in Python is a "class of a class." It defines how classes themselves are created, structured, and behave. Here are some key points to remember about metaclasses in Python:

1. **Class Creator**: Metaclasses are responsible for creating classes. They act as blueprints for how classes are constructed.

2. **Inheritance**: Just as classes define objects and their behavior, metaclasses define classes and their behavior. In other words, if a class is an instance of a metaclass, that class inherits the behavior specified by the metaclass.

3. **Class Modification**: Metaclasses allow you to modify class attributes and methods before the class is created. This provides a way to customize class behavior and structure at a higher level.

4. **`type` Metaclass**: The default metaclass in Python is `type`. It's responsible for creating all new classes. You can also create your own custom metaclasses by subclassing `type`.

5. **Metaclass Inheritance**: Just as classes can inherit from other classes, metaclasses can also inherit from other metaclasses. This hierarchy affects how attributes and behaviors are inherited and applied.

6. **`__metaclass__` Attribute**: You can set the `__metaclass__` attribute in a class to specify its metaclass. However, this is an older way of defining metaclasses, and using class inheritance from a custom metaclass is more common.

7. **Metaclass Methods**: Metaclasses can define special methods like `__new__` and `__init__`, which allow you to customize class creation and initialization.

8. **Powerful but Complex**: Metaclasses offer a high level of control and customization over class behavior, but they can also make code more complex and harder to understand. They're best used in cases where you need to enforce specific patterns across multiple classes.

Remember that while metaclasses are a powerful tool in Python, they might not be necessary for most everyday programming tasks. They are more commonly used in advanced scenarios and frameworks where fine-tuned class manipulation is required.

---

# Write a metaclass that automatically converts all attribute names to uppercase.

```python
# Define a custom metaclass named Meta
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        """
        Custom metaclass for automatically converting attribute names to uppercase.
        
        Args:
            class_name (str): The name of the class being created.
            bases (tuple): A tuple containing base classes of the class being created.
            attrs (dict): A dictionary containing attributes and methods defined in the class body.
        
        Returns:
            type: A new class with attributes' names converted to uppercase.
        """
        upper = {}
        for key, value in attrs.items():
            # Check if the attribute name starts with "__"
            if key.startswith("__"):
                upper[key] = value
            else:
                # Convert attribute name to uppercase and add to the upper dictionary
                upper[key.upper()] = value
        # Create and return a new class with modified attribute names
        return type(class_name, bases, upper)

# Define a class using the custom metaclass
class Adding(metaclass=Meta):
    """
    Class for demonstration purposes using a custom metaclass that converts attribute names to uppercase.
    """
    a: int = 5
    b: int = 6
    
    def sum(self):
        """
        Method to calculate the sum of attributes A and B.
        
        Returns:
            int: The sum of attributes A and B.
        """
        return self.A + self.B

# Main module execution
if __name__ == "__main__":
    # Create an instance of the Adding class
    adding = Adding()
    # Print the result of the 'sum' method
    print(adding.SUM())
```

In this code:

- The `Meta` metaclass is defined. It overrides the `__new__` method to create a new class with attribute names converted to uppercase.
- The `Adding` class is defined using the custom metaclass `Meta`. It demonstrates the functionality of the metaclass by having its attribute names converted to uppercase.
- The `sum` method calculates the sum of the attributes `A` and `B`, which are converted to uppercase.
- The main module execution section creates an instance of the `Adding` class and prints the result of calling the `sum` method, which should output the sum of `A` and `B` (i.e., `11`).

The provided documentation comments describe the purpose and functionality of each section of the code, making it clear what the code does and how it achieves its goals.


___

Reflection in Python refers to the ability of a program to examine and modify its own structure, behavior, or attributes at runtime. This involves inspecting and interacting with objects, classes, functions, and modules dynamically, rather than statically. Reflection allows you to access and manipulate various elements of a program without knowing their names or types beforehand.

Python provides several built-in tools and modules that facilitate reflection:

1. **`dir()` function:**
The `dir()` function returns a list of attributes and methods of an object. It includes both user-defined and built-in attributes. For example:
```python
obj = SomeClass()
attributes_and_methods = dir(obj)
print(attributes_and_methods)
```

2. **`getattr()` and `setattr()` functions:**
These functions allow you to get and set attributes of an object by name:
```python
obj = SomeClass()
value = getattr(obj, 'attribute_name')
setattr(obj, 'attribute_name', new_value)
```

3. **`inspect` module:**
The `inspect` module provides more advanced reflection capabilities, including functions to retrieve information about classes, functions, and objects. It's useful for more detailed introspection:
```python
import inspect

obj = SomeClass()
members = inspect.getmembers(obj)
print(members)
```

4. **`type()` function:**
The `type()` function returns the type of an object. It can be used to check if an object is an instance of a certain class:
```python
obj = SomeClass()
if type(obj) == SomeClass:
    print("Object is an instance of SomeClass")
```

5. **`isinstance()` function:**
The `isinstance()` function checks if an object is an instance of a specific class or a tuple of classes:
```python
obj = SomeClass()
if isinstance(obj, SomeClass):
    print("Object is an instance of SomeClass")
```

6. **Metaclasses:**
Metaclasses define the behavior of classes, including class creation and initialization. They allow you to customize class creation at the metaclass level, which can be considered advanced reflection.

Reflection can be powerful, but it should be used carefully due to its potential impact on code readability and security. Overusing reflection can make code harder to understand and maintain.