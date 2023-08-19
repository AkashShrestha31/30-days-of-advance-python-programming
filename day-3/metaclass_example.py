# 2. Write a metaclass that automatically converts all attribute names to
# uppercase.
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
