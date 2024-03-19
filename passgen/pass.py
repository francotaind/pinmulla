#!/usr/bin/python3

import random
import string

uppercase = random.sample(string.ascii_uppercase, k=3)
digit = [random.randint(0,9) for _ in range(3)]
special_char = random.sample(string.punctuation, k=3)
lowercase = random.sample(string.ascii_lowercase, k=3)

passwd = uppercase+digit+special_char+lowercase
random.shuffle(passwd)

pass_gen = "".join(map(str, passwd))

print(pass_gen)
