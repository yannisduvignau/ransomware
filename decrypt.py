#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []

excluded_files = {
    os.path.abspath('./requirements.txt'),
    os.path.abspath('./README.md'),
    os.path.abspath('./.gitignore'),
    os.path.abspath('./encrypt.py'),
    os.path.abspath('./decrypt.py'),
    os.path.abspath('./key.key')
}

excluded_dir = os.path.abspath('./env')

for root, _, filenames in os.walk('.'):
    if os.path.abspath(root).startswith(excluded_dir):
        continue

    for filename in filenames:
        filepath = os.path.join(root, filename)
        abs_path = os.path.abspath(filepath)

        if abs_path in excluded_files:
            continue

        files.append(filepath)

print(files)

with open('key.key', 'rb') as key_file:
    secret_key = key_file.read()
    
for file in files:
    with open(file, 'rb') as f:
        data = f.read()

    fernet = Fernet(secret_key)
    decrypted_data = fernet.decrypt(data)

    with open(file, 'wb') as f:
        f.write(decrypted_data)
        
print(f'Decrypted {len(files)} files.')
