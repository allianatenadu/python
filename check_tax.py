import time

def start_game():
    print("Welcome to the Dark Forest Adventure!")
    print("You find yourself in a dark forest...")
    print("You see two items on the ground: a MATCH and a FLASHLIGHT.")
    print("Which one do you want to pick up?")
    print("Type 'match' or 'flashlight' to choose.")

    choice = input().lower()

    if choice == "match":
        match_scenario()
    elif choice == "flashlight":
        flashlight_scenario()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def match_scenario():
    print("You pick up the match and strike it...")
    time.sleep(1)
    print("For an instant, the forest around you is illuminated.")
    time.sleep(1)
    print("You see a large grizzly bear, and then the match burns out.")
    time.sleep(1)
    print("Do you want to RUN, HIDE, or PLAY DEAD?")

    choice = input().lower()

    if choice == "run":
        print("You start running as fast as you can and manage to escape from the bear. Congratulations, you survived!")
    elif choice == "hide":
        print("You quickly hide behind a tree, hoping the bear didn't notice you. Luckily, it passes by without noticing you. Congratulations, you survived!")
    elif choice == "play dead":
        print("You drop to the ground and play dead. The bear sniffs around but eventually loses interest and leaves. Congratulations, you survived!")
    else:
        print("Invalid choice. Please try again.")
        match_scenario()

def flashlight_scenario():
    print("You pick up the flashlight and turn it on...")
    time.sleep(1)
    print("You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
    time.sleep(1)
    print("Do you want to FOLLOW the path, LOOK in the trees, or SHOUT for help?")

    choice = input().lower()

    if choice == "follow":
        print("You decide to follow the path and continue your journey deeper into the forest...")
        # Add more scenarios and choices here
    elif choice == "look":
        print("You cautiously look around in the trees but don't see anything. You decide to continue along the path.")
        # Add more scenarios and choices here
    elif choice == "shout":
        print("You shout for help, hoping someone nearby will hear you. You hear rustling in the bushes nearby...")
        # Add more scenarios and choices here
    else:
        print("Invalid choice. Please try again.")
        flashlight_scenario()

start_game()
