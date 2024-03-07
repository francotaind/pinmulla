import random
import string

password = []

for _ in range(2):
    password += (random.choice(string.ascii_uppercase))

p = (random.randint(100, 999))
password.append(p)

x = (random.choice(string.punctuation))
password.append(x)

for _ in range(3):
    password += (random.choice(string.ascii_lowercase))

pass_gen = "".join(str(element) for element in password)

print(pass_gen)
