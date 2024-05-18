import random
print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
options = ("Rock","Paper","Scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(Rock,Paper,Scissors):")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player =="Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again?(yes/no):").lower() == "yes":
        running = False

print("Thanks for playing!")
