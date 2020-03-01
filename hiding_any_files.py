import os
import json


secret_directory = 'filepath'
working_directory = 'filepath'
key_name = 'manage'

try:
    os.mkdir(secret_directory)
except FileExistsError:
    pass

operation = input('Please choose an operation:'
                  '\n1) Hide files'
                  '\n2) Get files back'
                  '\n> ')
while operation not in ("1", "2"):
    operation = input('Please choose an operation:'
                  '\n1) Hide files'
                  '\n2) Get files back'
                  '\n> ')

if operation == "1":
    saved_paths = []
    for dirpath, dirnames, filenames in os.walk(working_directory):
        for filename in filenames:
            if filename[:len(key_name)] == key_name and str(os.path.splitext(filename)[1]) in ('.py'):
                if dirpath != secret_directory:
                    original = {
                        'file_name': filename,
                        'dir_path': dirpath
                    }
                    saved_paths.append(original)
                    os.system(f'move "{os.path.join(dirpath, filename)}" "{secret_directory}"/')
            if len(saved_paths) > 0:
                with open(f'{secret_directory}/sec.json', 'w') as file:
                    json.dump(saved_paths, file, indent=2)

else:
    with open(f'{secret_directory}/sec.json', 'r') as file:
        python_data = json.load(file)
        for file_name in os.listdir(secret_directory):
            for file_dict in python_data:
                if file_name == file_dict['file_name']:
                    os.system(f'move \"{str(f"{secret_directory}/" + str(file_name))}\"'
                              f'\"{file_dict["dir_path"]}/\"')