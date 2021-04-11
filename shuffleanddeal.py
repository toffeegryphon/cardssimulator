import random

number_of_cards_dealt = int(input("How many cards do you want dealt?"))

while (number_of_cards_dealt > 52 or number_of_cards_dealt < 0) :
    print("That number is invalid. Please retry.")
    number_of_cards_dealt = int(input("How many cards do you want dealt?"))

suit = ["clubs", "diamonds", "hearts", "spades"]
random_number_0 = random.randint(0, 3)
random_number = random.randint(1, 13)
tuple_generator = ()

for x in range(number_of_cards_dealt):
    if ((random_number, suit[random_number_0]) in tuple_generator) :
        print("Doing Nothing Here")
    else:
        tuple_generator.append(random_number, suit[random_number_0)
        print(random_number, suit[random_number_0])
