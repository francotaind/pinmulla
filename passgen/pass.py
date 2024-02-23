import random
import string

print(random.randint(0, 20))
print(random.choice(string.ascii_lowercase))

#password = []
#password.append(9)
#print(f"{password}")

password = []

def passgen():
    for i in range(1, 7):
        password.append(i)
        return password

print(f"{password}")
passgen()
