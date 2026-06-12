from pathlib import Path

# Absolute path
# c:\Program Files\ MIcrosoft
# Relative path

# path = Path("ecommerce")
# print(path.exists())

# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)
