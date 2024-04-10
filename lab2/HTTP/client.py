import time
import requests
import sys
import utils

URL = 'http://localhost:5000/upload'

if __name__ == "__main__":
    file_size: int = int(sys.argv[1])
    file_name: str = utils.generate_file(file_size)
    with open(file_name, "rb") as file:    
        file_bytes = file.read()
    files = {'file': (file_name, file_bytes)}

    start = time.time()
    
    response = requests.post(URL, files=files)
    
    end = time.time()
    utils.remove_file(file_name)
    
    if response.status_code == 200:
        print(f"Time taken: {end-start:.10f}")
    else:
        print('Failed to upload file')