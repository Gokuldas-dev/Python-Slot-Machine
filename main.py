# PROGRAM: Python Slot Machine

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("The amount must be greater than zero!")
        else:
            print("Please enter a valid number.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")


def get_bet():
    while True:
        bet = input("What would you like to bet: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"The amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a valid number.")


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount. Your balance is: {balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Total bet is equal to {total_bet}.")


main()
