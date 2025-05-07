import random
print("Just for the Hint it's a flower")

words=["rose","sunflower", "tulip", "lily", "perwinkle", "lotus"]
chosen_word= random.choice(words)
words_display=["_" for _ in chosen_word]
attempts=8

print("Welcome to Hangman")

while attempts>0 and "_" in words_display:
    print("\n" +' '.join(words_display))
    guess=input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter==guess:
                words_display[index]=guess
    else:
        print("That's not the letter you Looser")
        attempts-=1

if "_" not in words_display:
    print("YAYYY you guessed the word")
    print(" " .join(words_display))
    print("You survived")

else:
    print(f"You ran out of attempts, the word was {chosen_word}")
    print("You lost")