# Welcome message and introduction to the game
print("Welcome to the Dark Forest Adventure!")
print("You find yourself in a dark forest...")
print("You see two items on the ground: a MATCH and a FLASHLIGHT.")
print("Which one do you want to pick up?")
print("Type 'match' or 'flashlight' to choose.")

# Player chooses between match and flashlight
choice = input().lower()

if choice == "match":
    # Player picks up the match
    print("You pick up the match and strike it...")

    # Consequence: Player sees a bear
    print("For an instant, the forest around you is illuminated.")
    print("You see a large grizzly bear, and then the match burns out.")

    # Player chooses how to react to the bear
    print("Do you want to RUN, HIDE, or PLAY DEAD?")
    choice = input().lower()

    if choice == "run":
        # Player chooses to run and survives
        print("You start running as fast as you can and manage to escape from the bear. Congratulations, you survived!")
    elif choice == "hide":
        # Player chooses to hide and survives
        print("You quickly hide behind a tree, hoping the bear didn't notice you. Luckily, it passes by without noticing you. Congratulations, you survived!")
    elif choice == "play dead":
        # Player chooses to play dead and survives
        print("You drop to the ground and play dead. The bear sniffs around but eventually loses interest and leaves. Congratulations, you survived!")
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")

    # Provide another level of choices
    print("You survived the encounter with the bear, but now you must decide what to do next.")
    print("Do you want to CONTINUE through the forest, EXPLORE the area around you, or REST and regain your strength?")
    choice = input().lower()

    if choice == "continue":
        # Player chooses to continue through the forest
        print("You gather your resolve and continue deeper into the forest, wary of further dangers...")
    elif choice == "explore":
        # Player chooses to explore the area
        print("You decide to take a closer look at your surroundings, searching for any useful resources or clues...")
    elif choice == "rest":
        # Player chooses to rest and regain strength
        print("Feeling weary from the encounter, you find a safe spot to rest and recover your strength...")
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")

elif choice == "flashlight":
    # Player picks up the flashlight
    print("You pick up the flashlight and turn it on...")

    # Consequence: Player hears a noise
    print("You see the pathway lit up in front of you, but you thought you also heard something off to the side.")

    # Player chooses how to react to the noise
    print("Do you want to FOLLOW the path, LOOK in the trees, or SHOUT for help?")
    choice = input().lower()

    if choice == "follow":
        # Player chooses to follow the path
        print("You decide to follow the path and continue your journey deeper into the forest...")

        # Consequence: Player encounters a hidden trap
        print("As you walk along the path, you step into a hidden trap!")
        print("Do you want to FREE yourself, CALL for help, or WAIT for rescue?")
        choice = input().lower()

        if choice == "free":
            # Player chooses to free themselves
            print("You manage to free yourself from the trap and continue on your way...")
        elif choice == "call":
            # Player chooses to call for help
            print("You call out for help, hoping someone nearby will come to your aid...")
        elif choice == "wait":
            # Player chooses to wait for rescue
            print("You decide to wait patiently, hoping someone will find you soon...")
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

    elif choice == "look":
        # Player chooses to look in the trees
        print("You cautiously look around in the trees but don't see anything. You decide to continue along the path.")

        # Consequence: Player finds a hidden treasure
        print("While walking along the path, something shiny catches your eye.")
        print("Do you want to INVESTIGATE the shiny object, LEAVE it alone, or RETURN to the main path?")
        choice = input().lower()

        if choice == "investigate":
            # Player chooses to investigate the shiny object
            print("You approach the shiny object and discover a hidden treasure!")
        elif choice == "leave":
            # Player chooses to leave the shiny object alone
            print("You decide to leave the shiny object undisturbed and continue on your way...")
        elif choice == "return":
            # Player chooses to return to the main path
            print("You decide to return to the main path and continue your journey from there...")
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

    elif choice == "shout":
        # Player chooses to shout for help
        print("You shout for help, hoping someone nearby will hear you. You hear rustling in the bushes nearby...")

        # Consequence: Player encounters a friendly animal
        print("As you approach the rustling bushes, a friendly fox emerges from the underbrush.")
        print("Do you want to FOLLOW the fox, IGNORE it and continue, or RETURN to the main path?")
        choice = input().lower()

        if choice == "follow":
            # Player chooses to follow the fox
            print("You decide to follow the fox, curious about where it might lead...")
        elif choice == "ignore":
            # Player chooses to ignore the fox
            print("You decide to ignore the fox and continue on your current course...")
        elif choice == "return":
            # Player chooses to return to the main path
            print("You decide to return to the main path and continue your journey from there...")
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

    else:
        # Invalid choice
        print("Invalid choice. Please try again.")

else:
    # Invalid choice
    print("Invalid choice. Please try again.")
