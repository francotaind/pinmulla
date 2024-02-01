MAX_LINES = 3
MAX_STAKE = 1000
MIN_STAKE = 50

def deposit():
    while True:
        amount = input("what would you like to deposit? KSH ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount greater than 0")
        else:
            print("please enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid no of lines")
        else:
            print("enter a number")
    return lines

def get_stake():
    while True:
        stake = input("enter stake amount ")
        if stake.isdigit():
            stake = int(stake)
            if MIN_STAKE <= stake <= MAX_STAKE:
                break
            else:
                print(f"amount must be between {MIN_STAKE} - {MAX_STAKE}")
        else:
                print("enter stake")
    return stake



def main():
    balance = deposit()
    lines = get_number_of_lines()
    stake = get_stake()
    total_bet = stake * lines
    print(balance, lines, stake)
    print(f"you are staking KSH{stake} on {lines} lines. Total bet is {total_bet}")

main()
