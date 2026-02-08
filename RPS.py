#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  play_response = 'Y'

  while play_response.upper() == 'Y':
    progr = random.choice(['R', 'P', 'S'])

    user = input("Choose Rock (R), Paper (P), or Scissors (S): ").upper()

    if user not in ['R', 'P', 'S']:
      print("INvalid choice. Please choose R, P, or S")
      continue

    print(f"Program choose: {progr}")

    if user == progr:
      print("It's a tie.")
      ties +=1
    elif (user == 'R' and progr == 'S') or \
             (user == 'P' and progr == 'R') or \
             (user == 'S' and progr == 'P'):
            print("You win!")
            wins += 1
    else:
       print("You loose.")
       losses +=1
    play_response = input("Would you like to play again? (Y/N)").upper()

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
