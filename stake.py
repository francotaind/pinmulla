MAX_STAKE = 1000
MIN_STAKE = 50

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