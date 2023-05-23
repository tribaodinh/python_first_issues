#hangman and the words are from another file

import random

def the_person(counter):
    if counter == 1:
        print(" |")
    if counter == 2:
        print(" |")
        print(" 0")
    if counter == 3:
        print(" |")
        print(" 0")
        print(" |")
    if counter == 4:
        print(" |")
        print(" 0")
        print("/|")   
    if counter == 5:
        print(" |")
        print(" 0")
        print("/|\\")
    if counter == 6:
        print(" |")
        print(" 0")
        print("/|\\")
        print("/")
    if counter == 7:
        print(" |")
        print(" 0")
        print("/|\\")
        print("/ \\")

def getting_words_from_file():

    global guess_counter
    guess_counter = 0
    #make empty list
    list = []
    #opening file and reading each line
    file1 = open("hangman_words.txt", 'r')
    lines = file1.readlines()

    #break up each line to each word then put them in a list
    for line in lines:
        for word in line.split():
            list.append(word)
    #return list with words
    return list
       
def hangman(list_of_words):
    #get the list and pick a random word from it
    hangman_word = random.choice(list_of_words)

    empty_word = []
    previous_guesses = []
    global guess_counter
    #fill up the empty_word list with blanks
    for blank in hangman_word:
        empty_word.append("_")

    
    while(True):
        
        #print the hangman
        the_person(guess_counter)
        #if used up 7 try then you fail
        if guess_counter >= 7:
            print("you have lost")
            break
        
        #print how many guesses left
        print(f"you have {7 - guess_counter} left")

        #print out the list of empty_word and what remaining words you have left
        for letter in empty_word:
            print(letter, end =' ')

        #print previous guesses
        print("\nprevious guesses:", end=" ")

        for index_old_letters in range(len(previous_guesses)):
            print(f"{previous_guesses[index_old_letters]},", end=" ")

        #asking for guess
        letter_guess = input("\nwhat is your guess: ")

        if letter_guess in empty_word:
            print("you have already guessed that correct letter, try a different one")
            continue
        previous_guesses.append(letter_guess)


        #if guess wrong, add 1 to counter
        if letter_guess not in hangman_word:
            print("incorrect guess")
            guess_counter += 1
            continue
        
        #use enumerate (gets both index and letter) then if each guess is right, 
        #place right letter in the right index of empty_word list 
        for index, letter in enumerate(hangman_word):       
            if letter_guess == letter:
                empty_word[index] = letter_guess

        #if no blanks in empty_word then you win
        if "_" not in empty_word:
            print("congratulations, you win")
            break

    while(True):
        answer = input("Do you want to play again(enter yes or no): ")
        if answer == "yes":
            hangman(getting_words_from_file())
        if answer == "no":
            print("thank you for playing")
            exit()
   


hangman(getting_words_from_file())
