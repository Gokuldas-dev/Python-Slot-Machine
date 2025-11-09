# This is the [PROGRAM FOR Python-Slot-Machine]
#Global varibale go here --
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit(): # this is a function to check the amount is digit or not and to make it as a digit (integer)
  while True:
    amount = input("what would you like to deposit : ")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0 :
        break
      else:
        print ("The amount must be greater than zero ! ")  # this should be greater than zero 
    else:
      print ("Please enter a number :") 

  return amount  #if true the amount will be submited and will be a digit.

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on  (1-" + str(MAX_LINES) + ")" )
    if lines.isdigit():
      lines = int(lines)
      if 1<= lines <= MAX_LINES:
        break
      else:
        print ("Enter the valid number of lines :  ")  # this should be teh valid range of numbers 
    else:
      print ("Please enter a number :") 

  return lines 

def get_bet():
  while True:
    bet = input("what would you like to bet : ")
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print(f"The Amount must be between {MIN_BET} - {MAX_BET} ")  # this should be between those values  
    else:
      print("Please enter a number :") 

    return bet

# this is the main function 
def main():
  balance = deposit()
  lines = get_number_of_lines()
  bet = get_bet()
  print(balance,lines,bet)
 


main()
