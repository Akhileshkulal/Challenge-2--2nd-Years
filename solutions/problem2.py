# problem2.py
# Reverse string, remove every 3rd char, shift ASCII +2, count vowels

vowels = set("aeiouAEIOU")

# Read input string and remove any trailing newline or spaces
with open("inputs/input2.txt") as f:
    s = f.read().strip()

# Step 1: Reverse
s = s[::-1]

# Step 2: Remove every 3rd character (1-based)
s = ''.join(c for i, c in enumerate(s) if (i + 1) % 3 != 0)

# Step 3: Shift ASCII +2
s = ''.join(chr(ord(c) + 2) for c in s)

# Step 4: Count vowels
clue2 = sum(1 for c in s if c in vowels)

print("Clue 2:", clue2)
