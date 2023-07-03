import random

spiller_valg = input("rock paper scissors shoot (rock, paper, scissors): \n")
possible_choices = ["rock", "scissors", "paper"]

pc_valg = random.choice(possible_choices)


print(f"\n you chose {spiller_valg}, CPU chose {pc_valg} \n")

if spiller_valg == pc_valg:
    print(f"begge valgte{spiller_valg}. ingen vinnere")
elif spiller_valg == "rock":
    if pc_valg == "scissors":
        print ("rock crushes scissors. you win!")
    else:
        print("paper covers rock. you loose")
elif spiller_valg == "scissors":
    if pc_valg == "paper":
        print ("scissors cuts paper. you win")
    else:
        print("rock crushes scissors. you loose")
elif spiller_valg == "paper":
    if pc_valg == "rock":
        print ("paper covers rock. you win")
    else:
        print("scissors cuts paper. you loose")