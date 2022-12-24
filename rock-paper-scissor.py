import random
def get_choices():
  player_choice = input("Enter a chioce (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice, "computer" : computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}.")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "Scissors":
      return "Rock smashes Scissors! You win!"
    else:
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cut paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissor cuts paper! You win!"
    else:
      return "Rock smases scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)