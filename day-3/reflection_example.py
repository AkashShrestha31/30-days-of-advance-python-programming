import inspect


class Dog():
    """
    A simple class representing a dog with attributes and methods.
    """
    x: int = 1  # An integer attribute 'x'
    y: int = 2  # An integer attribute 'y'
    
    def sum(self):
        """
        Method to calculate the sum of attributes x and y.
        
        Returns:
            int: The sum of attributes x and y.
        """
        return self.x + self.y
    
    
# Main module execution
if __name__ == "__main__":
    # Create an instance of the Dog class
    dog = Dog()
    
    # Get a list of attributes and methods using dir()
    list_of_attr = dir(dog)
    print("List of attributes and methods:", list_of_attr)
    
    # Get the value of attribute 'x' using getattr()
    value = getattr(dog, 'x')
    print("Value of attribute 'x':", value)
    
    # Set a new value for attribute 'x' using setattr()
    setattr(dog, 'x', 5)
    print("New value of attribute 'x':", dog.x)
    
    # Get members (attributes and methods) of the object using inspect
    insp = inspect.getmembers(dog)
    print("Detailed inspection of object:", insp)
