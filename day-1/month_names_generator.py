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
