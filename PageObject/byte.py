import os

def check_null_bytes(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        if b'\x00' in content:
            print(f"Null byte found in {file_path}")

# Укажите путь к вашей папке с проектом
for root, dirs, files in os.walk(r"C:\Users\Anastasia\AutoTests\PageObject"):
    for file in files:
        if file.endswith('.py'):
            check_null_bytes(os.path.join(root, file))