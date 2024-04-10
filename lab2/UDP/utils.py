import os

def generate_file(n: int):
    file_name = f'{n}_byte_file.bin'
    file_size = 1 << n # 2^n

    with open(file_name, "wb") as file:
        file.write(os.urandom(file_size))
    return file_name

def remove_file(file_name: str):
    os.remove(file_name)
    
