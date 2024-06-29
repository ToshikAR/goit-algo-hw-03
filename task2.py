#task2
#генерує набір унікальних випадкових чисел у межах заданих параметрів 

import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or quantity > (max - min + 1): return[]
    return sorted(random.sample(range(min, max+ 1), quantity))

print(f"Your ticket numbers: {get_numbers_ticket(1, 255, 7)}")