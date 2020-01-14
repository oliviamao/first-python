from random import choice

#another way:
#import random
#random.choice()
#choice()

questions = ["Why is the sky blue?","Why is the star briliant?","Why is the night dark?"]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh...okay")
