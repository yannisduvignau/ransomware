#  Ransomware

### 1. Create a Python virtual environment (using Python 3)
```bash
    python3 -m venv env
```

### 2. Activate the virtual environment
```bash
    source env/bin/activate
```

### 3. Prepare the requirements file and install dependencies
```bash
    echo "cryptography" > requirements.txt
    pip install -r ./requirements.txt
```

### 4. Create a .gitignore file to avoid committing sensitive files
```bash
    echo ".gitignore\nenv/\nrequirements.txt\n.env*\n*.log\nkey.key" > .gitignore
```

### 5. Run encrypt
```bash
    python3 encrypt.py
```

### 6. Run decrypt
```bash
    python3 decrypt.py
```

### 7. Deactivate the virtual environment
```bash
    deactivate
```