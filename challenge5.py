#this is a sequence of list where we have to find whether the word which random module make words of user matches with it or not...

#let's begin the program....

word_list = ["ardvark","baboon","camel"]

import random
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
print(chosen_word)