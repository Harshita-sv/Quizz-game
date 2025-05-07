import random
words=["sky", "star", "planets"]
random_word= random.choice(words)
new_word= ["_" for _ in random_word]
attempts=8

while attempts>0 and "_"  in new_word:
    print(" ".join(new_word))
    guess=input("Enter you guess").lower()
    if guess in random_word:
        for index, letter in enumerate(random_word):
            if letter==guess:
                new_word[index]=guess


    else:
        print("That's not the letter duhh")        
        attempts-=1
        
if "_" not in random_word:
    print("Yaa you won")
else:
    print("You lose")

