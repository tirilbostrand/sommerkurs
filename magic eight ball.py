import random

#input("hva lurer du på?")

#svar = ("ja", "nei", "kansje", "spør meg igjen etterpå", "definitivt", "absålutt ikke", "absålutt", "nope")
#svar2 = random.choice(svar)

#print: (svar2)



name = "bob"
answer = ""

random_number = random.randint(1,8)

question = input("what do you wish to seek the answer to?")

if random_number == 1:
    answer = "yes"
elif random_number == 2:
    answer = "no"
elif random_number == 3:
    answer = "maybe"
elif random_number == 4:
    answer = "ask me again later"
elif random_number == 5:
    answer = "nope"
elif random_number == 6:
    answer = "YYYAAAAAAAAAAS, QUEEN!"
elif random_number == 7:
    answer = "perhaps"
elif random_number == 8:
    answer = "im busy rn"
else:
    answer = "srry, smthn went wrng"

print(f"\n hi {name} the answer to ur question is: {question} is {answer}\n")