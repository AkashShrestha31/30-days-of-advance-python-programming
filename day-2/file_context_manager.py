class File:
    """
    A context manager for file handling.

    Args:
        filename (str): The name of the file to work with.
        mode (str, optional): The mode in which to open the file (default is 'r').

    Usage:
        with File("user.csv") as file:
            content = file.read()
            print(f"Working on {file}...")
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
        
