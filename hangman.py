import random

from  hangman_words_art_logo import word_list
from hangman_words_art_logo import hangman
from hangman_words_art_logo import logo

lives = 6
print(logo)

choose_word = random.choice(word_list)
print(choose_word)

placeholder = ""
word_length = len(choose_word)
for position in range(word_length):
    placeholder += "_"
print("word to guess : " + placeholder)

game_over = False

current_letter = []

while not game_over :
    print(f"******************** {lives} /6 LIVES LEFT ***********************")
    guess = input("guess the letter : ").lower()
    if guess in current_letter:
        print(f"youhave already guessed {guess}")
   

    display = ""

    for letter in choose_word:
        if letter == guess:
            display += letter
            current_letter.append(guess)
        elif letter in current_letter :
            display += letter
        else:
            display += "_"
            
    print("word to guess : " + display)
    
    if guess not in choose_word:
        lives -= 1
        print(f"you guessed {guess}, that is not in the word. you lost a life.")
        if lives == 0:
            game_over = True
            print(f"*******************IT WAS {choose_word} You Lost!*********************")
    
    if "_" not in display:
        game_over = True
        print("************************You Win!**************************")
        
    print(hangman[lives])
        


    