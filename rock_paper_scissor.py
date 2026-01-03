import random

# dictionary to determine the winner

emojis = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

choices = ['rock', 'paper', 'scissors']

while True:
 user_choice = input("Enter rock, paper, or scissors: ").lower()
 if user_choice not in choices:
     print("Invalid choice. Please choose rock, paper, or scissors.")
 continue
 computer_choice = random.choice(choices)
 
 print(f"Computer chose: {computer_choice}")
 print(f"You chose: {user_choice} {emojis[user_choice]}")
 print(f"Computer chose: {computer_choice} {emojis[computer_choice]}")
 
 if user_choice == computer_choice:
     print("It's a tie!")
 elif (user_choice == 'rock' and computer_choice == 'scissors') or \
      (user_choice == 'paper' and computer_choice == 'rock') or \
      (user_choice == 'scissors' and computer_choice == 'paper'):
     print("You win!")
 else:
     print("Computer wins!")
 
 shoulsd_continue = input("Do you want to play again? (yes/no): ").lower()
 if shoulsd_continue == 'yes':
     # Restart the game
     exec(open(__file__).read())