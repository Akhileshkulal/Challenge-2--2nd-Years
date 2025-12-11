# problem3.py
# Simulate state machine and count how many reach DONE

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

# Read numbers
with open("inputs/states.txt") as f:
    numbers = [int(x) for x in f.read().split()]

clue3 = 0

for n in numbers:
    # Check prime first
    if is_prime(n):
        # direct jump to DONE
        clue3 += 1
    elif n % 2 == 0:
        # Even: advance step by step until DONE (3 steps)
        clue3 += 1
    else:
        # odd composite: does not reach DONE
        pass

print("Clue 3:", clue3)
