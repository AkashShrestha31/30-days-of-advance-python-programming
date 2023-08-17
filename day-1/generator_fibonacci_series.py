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


# Create a generator instance for the Fibonacci sequence
fibonacci_gen = fibonacci_sequence()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    next_fibonacci = next(fibonacci_gen)  # Get the next Fibonacci number
    print(next_fibonacci)  # Print the generated Fibonacci number
