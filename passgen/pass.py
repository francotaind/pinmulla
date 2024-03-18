#!/usr/bin/python3

import random
import string

password = []

for _ in range(3):
    password += (random.choice(string.ascii_uppercase))

p = (random.randint(100, 999))
password.append(p)

for _ in range(3):
    password += (random.choice(string.punctuation))

for _ in range(3):
    password += (random.choice(string.ascii_lowercase))

pass_gen = "".join(str(element) for element in password)

print(pass_gen)
