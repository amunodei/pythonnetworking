import random
#Loop
while True:
 choice = input("Do you want to roll the dice? (yes/no): ").lower()
 if choice == 'yes':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"You rolled a {die1} and a {die2}. Total: {total}")
 elif choice == 'no':
      print("Thanks for playing!")
      break
 else:
        print("Invalid input. Please enter 'yes' or 'no'.")
 