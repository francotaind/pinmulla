#!/usr/bin/env python3
import random
from deposit import deposit
from stake import get_stake
from play import check_winnings, get_spin, print_machine, get_number_of_lines, spinned 

def main():
    balance = deposit()
    while True:
        print(f"current bal is {balance}")
        spin = input("print enter to play(q to quit)")
        if spin == "q":
            break
        balance += spinned(balance)

    print(f"you left with {balance}")

main()
