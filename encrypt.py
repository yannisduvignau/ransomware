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

key = Fernet.generate_key()

with open('key.key', 'wb') as key_file:
    key_file.write(key)
    
for file in files:
    with open(file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file, 'wb') as f:
        f.write(encrypted_data)
        
print(f'Key saved to key.key. Encrypted {len(files)} files.')
