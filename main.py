import functions

def main():

    functionsclass = functions.fruit_machine_class()
    balance = functionsclass.deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += functions.game(balance)

    print(f"You left with ${balance}")

main()