# Modules + converters.py

from utils import find_max  # or
import converters
from converters import kg_to_lbs

kg_to_lbs(70)

print(converters.kg_to_lbs(100))


# Exercise

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)
