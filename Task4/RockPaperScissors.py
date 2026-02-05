import random

def display_menu():
    print("\n==============================")
    print(" ROCK - PAPER - SCISSORS GAME ")
    print("==============================")
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("==============================")

def get_user_choice():
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        display_menu()

        user_choice = get_user_choice()
        computer_choice = random.randint(1, 3)

        user_name = get_choice_name(user_choice)
        computer_name = get_choice_name(computer_choice)

        print(f"\nYou chose: {user_name}")
        print(f"Computer chose: {computer_name}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("Result: It's a TIE")
        elif result == "user":
            print("Result: You WIN")
            user_score += 1
        else:
            print("Result: Computer WINS")
            computer_score += 1

        print("\n--- SCOREBOARD ---")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing")
            break

# Start the game
play_game()
