import threading
import requests


def download_and_save_file(url, file_index):
    """
    Download a file from the given URL and save it with an index-based filename.
    
    Args:
        url (str): The URL of the file to be downloaded.
        file_index (int): Index for generating the filename.
    """
    print(f"Starting downloading file at index {file_index}")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"images/file_{file_index}.jpg", "wb") as file:
            file.write(response.content)
        print(f"Download completed for file at index {file_index}")
    else:
        print("Error loading file")
    

if __name__ == "__main__":
    threads = []
    file_url = "https://picsum.photos/200/300"
    
    for index in range(10):
        thread = threading.Thread(target=download_and_save_file, args=(file_url, index))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
