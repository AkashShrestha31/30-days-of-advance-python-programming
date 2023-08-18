
#context manager allow us porperly manage resources
 
class File:
    def __init__(self, *args, **kwargs):
        pass
    
    def __enter__(self):
        print("opening file....")
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing file...")
        pass
    
    
if __name__ == "__main__":
    with File() as file:
        print("processing")