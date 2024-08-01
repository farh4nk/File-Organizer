import os
import shutil

path = input("Enter Path to be organized: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    
    if os.path.exists(f'{path}/{extension}'):
        shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
    else:
        os.makedirs(f'{path}/{extension}')
        shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
