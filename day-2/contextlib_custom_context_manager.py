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


if __name__ == "__main__":
    try:
        with custom_context_manager("information.csv") as file:
            content = file.read()
            print(content)
            print("--------------------------------------------------------")
            
    except FileNotFoundError as e:
        print(f"Exception: {e}")
