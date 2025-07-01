from typing import List

def average(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Przykład:
# print(average([1.5, 2.5, 3.0]))  # Wynik: 2.333...
