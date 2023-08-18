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
            yield file
    finally:
        pass
    
 
if __name__ == "__main__":
    with read_file("information.csv") as file:
        for line in file:
            print(line, end='')
