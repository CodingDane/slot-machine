MAX_LINES = 3

def deposit():
  while True:
    amount = input("Enter the amount you want to deposit: ¥")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please enter a positive number.")
    else:
        print("Please enter a number.")
    return amount

def get_number_of_lines():
   while True:
    lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")?")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please enter a positive number.")
    else:
        print("Please enter a number.")
    return amount

def main():
    balance = deposit()

main()
