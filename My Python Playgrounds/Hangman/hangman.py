import random
from words import words, kata, clue
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word.upper()

def hangman():
    difficult = input("Pilih tingkat kesulitan tinggi atau sedang: ")
    if difficult == "tinggi":
        word = get_valid_word(words)
    elif difficult == 'sedang':
        word = get_valid_word(kata)
    else:
        difficult = random.choices(["words", "kata"])
        for word in difficult:
            difficult = word
            if difficult == "words":
                print("Tingkat kesulitan terpilih ke tinggi secara otomatis.")
            elif difficult == "kata":
                print("Tingkat kesulitan terpilih ke sedang secara otomatis.")
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have ", lives, "lives left and You have used these letters: ", ' '.join(used_letters))
        if difficult == 'sedang' or 'kata': 
            print("The clue is: ", clue)
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives -1 # takes away a life if wrong
                print('\nYour letter', user_letter, ' is not in the word')
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
    
    # get here when len(word_letters) ==  0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == "__main__":
    hangman()