import random

MAX_LINES = 3 # global function allowing the max lines to be 3 
MAX_BET = 100 # global function making the max bet amount £100
MIN_BET = 1 # global function making the min bet £1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # _ is an annonymous variable 
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): 
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.replace('.', '', 1).isdigit() and amount.count('.') <= 1:
            amount = float(amount) # turns to integer - default is string 
            if amount > 0:
                break # if it is a valid number, break out of while loop, if not continue in loop
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number")

    return amount 

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines) # turns to integer - default is string 
            if 1 <= lines <= MAX_LINES:
                break # if it is a valid number, break out of while loop, if not continue in loop
            else: 
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines   

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? £")
        if amount.replace('.', '', 1).isdigit() and amount.count('.') <= 1:
            amount = float(amount) # turns to integer - default is string 
            if MIN_BET <= amount <= MAX_BET:
                break # if it is a valid number, break out of while loop, if not continue in loop
            else: 
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}")
        else:
            print("Please enter a valid number")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds, your current balance is £{balance:.2f}")
        else:
            break 

    print(f"You are betting £{bet:.2f} on {lines} lines. Your total bet is: £{total_bet:.2f}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won: £{winnings:.2f}!")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit() 
    while True:
        print(f"Current balance is £{balance:.2f}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with £{balance:.2f}")

main()
