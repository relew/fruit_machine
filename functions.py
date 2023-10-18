import random
import config


class fruit_machine_class:

    def check_winnings(self,columns,lines,bet,values):
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
                winning_lines.append(line+1)
        
        return winnings,winning_lines



    def get_fruit_machine_spin(self,rows,cols,symbols):
        all_symbols = []
        columns =[]

        for symbol,symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        for _ in range(cols):
            current_symbols = all_symbols[:]
            column = []

            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)

        print(columns)
        return columns

    def print_fruit_machine(self,columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(column) -1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")

            print()


    def deposit(self):
        while True:
            amount = input("What would you like to deposit? $")

            if amount.isdigit():
                amount = int(amount)

                if amount > 0:
                    break
                else: 
                    print("Amount must be more than 0.")
            else:
                print("Please enter a number.")
        return amount

    def get_num_of_lines(self):
        while True:
            lines = input("Enter the number of lines to bet on(1-" + str(config.MAX_LINES) + ")? ")

            if lines.isdigit():
                lines = int(lines)

                if lines >= 1 & lines <= config.MAX_LINES:
                    break
                else: 
                    print("Lines must be more than 1 and less than " + str(config.MAX_LINES +1) +".")
            else:
                print("Please enter a number.")
        return lines

    def get_bet(self):
        while True:
            amount = input("How much would you like to bet on each line? $")

            if amount.isdigit():
                amount = int(amount)

                if config.MIN_BET <= amount <= config.MAX_BET:
                    break
                else: 
                    print("Bet amount must be more than "+str(config.MIN_BET-1)+" and less than " + str(config.MAX_BET +1) +".")
            else:
                print("Please add your bet amount.")
        return amount  

def game(balance):
    functionsclass = fruit_machine_class()
    lines = functionsclass.get_num_of_lines()
    while True:
        bet = functionsclass.get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don not have enought to bet that amount, your current balance is: ${balance}")

        else:
            break

    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${bet * lines}.")

    slots = functionsclass.get_fruit_machine_spin(config.ROWS,config.COLS,config.symbol_count)
    functionsclass.print_fruit_machine(slots)
    winnings,winning_lines = functionsclass.check_winnings(slots,lines,bet,config.symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet 