import random
from words import phrase_list


def get_phrase():
    phrase = random.choice(phrase_list)
    return phrase.upper()

def play(phrase):
    phrase_completion = "_" * len(phrase)
    guessed = False
    guessed_letters = []
    guessed_phrases = []
    tries = 7
    print("Welcome to Head Space.")
    print(display_something(tries))
    print(phrase_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Waiting for something to happen? ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already collected that letter", guess)
            elif guess not in phrase:
                print(guess, "is in the void.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Letter", guess, "is collected.")
                guessed_letters.append(guess)
                phrase_as_list = list(phrase_completion)
                indices = [i for i, letter in enumerate(phrase) if letter == guess]
                for index in indices:
                    phrase_as_list[index] = guess
                phrase_completion = "".join(phrase_as_list)
                if "_" not in phrase_completion:
                    guessed = True
        elif len(guess) == len(phrase) and guess.isalpha():
            if guess in guessed_phrases:
                print("This one is done.", guess)
            elif guess != phrase:
                print(guess, "is incorrect.")
                tries -= 1
                guessed_phrases.append(guess)
            else:
                guessed = True
                phrase_completion = phrase
        else:
            print("Again")
        print(display_something(tries))
        print(phrase_completion)
        print("\n")
    if guessed:
        print("Welcome to Black Space")
    else:
        print("Welcome to White Space")



def display_something(tries):
    stages = [  # 7/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |   |  /\\  |
                   |   |  \\/  |
                   |   |      |
                   |   |/\\  /\\|
                   |      \\/
                   |
                   -
                """,
                # 6/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |   |  /\\  |
                   |   |  \\/  |
                   |   |      |
                   |   |/\\  /\\|
                   |
                   |
                   -
                """,
                # 5/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |   |  /\\  |
                   |   |  \\/  |
                   |   |      |
                   |
                   |
                   |
                   -
                """,
                # 4/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |   |  /\\  |
                   |   |  \\/  |  
                   |
                   |
                   |
                   |
                   -
                """,
                # 3/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |   |  /\\  | 
                   |
                   |
                   |
                   |
                   |
                   -
                """,
                # 2/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |   -      -
                   |  
                   |     
                   |
                   |
                   |
                   |
                   -
                """,
                # 1/7 "Something" form
                """
                   --------
                   |      |
                   |     ____
                   |    
                   |      
                   |     
                   |
                   |
                   |
                   |
                   -
                """,
                # 0/7 "Something" form
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def main():
    phrase = get_phrase()
    play(phrase)
    while input("Wake up? (Y/N) ").upper() == "N":
        phrase = get_phrase()
        play(phrase)

if __name__ == '__main__':
    main()