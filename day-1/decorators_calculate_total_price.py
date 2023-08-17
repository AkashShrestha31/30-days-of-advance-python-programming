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
  
