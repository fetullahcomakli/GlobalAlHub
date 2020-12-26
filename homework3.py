import random
#from words import word_list
word_list=["cat","dog","elephant","chicken","giraffe"]

user=str(input("Profile Name : ")).upper()

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_display = "_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=5
    print("Welcome %s :)\nYou have %d attempts.\nWords are just animal names!\nLets start.Word have %d letters!"%(user,tries,len(word)))
    print(word_display)
    print("\n")

    while not guessed and tries > 0:
        guess=input("Make a guess :").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You tried: {guess}!")
            elif guess not in word:
                tries-=1
                print(f"Letter {guess} is not in the word.You have total {tries} guess!")
                guessed_letters.append(guess)
            else:
                print(f"Letter {guess} is in the word.")
                guessed_letters.append(guess)
                world_as_array=list(word_display)
                indices =[i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    world_as_array[index]=guess
                word_display="".join(world_as_array)
                if "_" not in word_display:
                    guessed=True

        elif len(guess)==len(word) and guess.isalpha():
            if guess==word:
                guessed=True
                word_display=word
            elif guess in guessed_words:
                print(f"You tried : {guess} !")
            else:
                print("Your answer is not correct!")
                guessed_words.append(guess)
                tries -= 1

        else:
            print("Invalid guess!")
        print(word_display)
        print("\n")

    if guessed:
        print("Congratulations %s !" %(user))
    else:
        print(f"Unfortunately ... The correct answer : {word}")

def main():
    word=get_word()
    play(word)

main()

