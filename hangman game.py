
"""My Guide
First create different categories for guessing the word.
Then create a function that tells us about the word and replaces it with character if present.
Take user input and substitute it with character.
Add hints if needed if Hints used remove an attempt (Hints can only be used twice)."""

import random

#categories

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'black', 'white']
animals = ['cat', 'dog', 'elephant', 'tiger', 'lion', 'giraffe', 'zebra', 'panda', 'rabbit', 'kangaroo']
countries = ['india', 'france', 'japan', 'brazil', 'australia', 'canada', 'germany', 'italy', 'china', 'egypt']
sports = ['cricket', 'football', 'tennis', 'basketball', 'badminton', 'volleyball', 'hockey', 'golf', 'swimming', 'boxing']
vehicles = ['car', 'bike', 'bus', 'train', 'truck', 'scooter', 'bicycle', 'airplane', 'boat', 'helicopter']
shapes = ['circle', 'square', 'triangle', 'rectangle', 'hexagon', 'pentagon', 'octagon', 'ellipse', 'parallelogram', 'rhombus']
musical_instruments = ['guitar', 'piano', 'violin', 'drums', 'flute', 'saxophone', 'trumpet', 'tabla', 'harmonica', 'cello']
languages = ['english', 'hindi', 'spanish', 'french', 'german', 'japanese', 'korean', 'italian', 'russian', 'portuguese']
planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
occupations = ['doctor', 'engineer', 'teacher', 'artist', 'chef', 'pilot', 'nurse', 'lawyer', 'architect', 'scientist']
desserts = ['cake', 'icecream', 'brownie', 'pudding', 'pie', 'cupcake', 'donut', 'waffle', 'mousse', 'tart']
clothing = ['shirt', 'jeans', 'jacket', 'skirt', 'dress', 'sweater', 'shorts', 'blazer', 'coat', 'scarf']
furniture = ['chair', 'table', 'sofa', 'bed', 'wardrobe', 'desk', 'bookshelf', 'stool', 'cabinet', 'bench']
emotions = ['happy', 'sad', 'angry', 'excited', 'nervous', 'confused', 'bored', 'surprised', 'calm', 'proud']
gadgets = ['smartphone', 'laptop', 'tablet', 'smartwatch', 'camera', 'earbuds', 'printer', 'speaker', 'monitor', 'keyboard']
category=[colors,animals,countries,sports,vehicles,shapes,musical_instruments,languages,planets,occupations,desserts,clothing,furniture,emotions,gadgets]

def game(number):
    help=2
    category_name=category[number-1]
    word = random.choice(category_name)

    attempt=len(word)+5
    print("Number of attempts you have: ",attempt)
    print("\n")
    print("The below word has",len(word),"letters")
    display = ['-' for _ in word]
    print(' '.join(display))
    while attempt>0 and ''.join(display)!=word:
        print('\n')
        character=input("Enter a character (or type hint for help) ::: ").lower()
        while not (character == 'hint' or (len(character) == 1 and character.isalpha())):
            print("Enter only a SINGLE LETTER")
            print('\n')
            character=input("Enter a character (or type hint for help) ::: ").lower()
        print('\n')

        if (character == 'hint') and (help>0):
            
            ind=int(input("Which Character do u need help with :: "))
            print('\n')
            if display[ind-1]=='-':
                display[ind-1]=word[ind-1]
                for idx, char in enumerate(word):
                    if char == word[ind-1] and idx != ind-1:
                        display[idx] = word[ind-1]
                print(' '.join(display))
                help-=1
            elif display[ind-1]!='-':
                print("You already guessed that letter")

            
        elif (character == 'hint') and (help==0):
            print("You have used all your hints")
            print('\n')
            continue

        elif character != 'hint':
            if character in display:
                print("You already guessed that letter")
                print('\n')
                continue
            if ''.join(display)!=word:
                if character in word:
                    revealed = False
                    for index, letter in enumerate(word):
                        if letter == character and display[index] == '-':
                            display[index] = character
                            revealed = True
                            print('\n')
                            print(' '.join(display))
                            print('\n')
                if character not in word:
                    revealed = False
                    print("Opps! Wrong Guess")
                    attempt -= 1
                    print('\n')
                    print(' '.join(display))
                    print('\n')
        

                if revealed:
                    print("YAYYYY! You Got it :)\nKEEP GOING")
            
                
        print(f"Remaining Attempts: {attempt}")

    print('\n')
    if ''.join(display)==word:
        
        print("YAYYYY! You Got it :)\nYou won the game")
    else:
        print("You lost the game")
        print(f"The word was {word.upper()}")
   
print("\n")
print("WELCOME TO HANGMAN GAME")
print("\n")
print("HOW TO PLAY")
print("\n")
print("1) You will be given a category (like Animals, Sports, Countries, etc.")
print("2) A secret word from this category will be selected and shown to you as dashes (_ _ _), each dash representing a hidden letter.")
print("3) Your goal is to guess the correct word by suggesting one letter at a time.")
print("4) Every time you guess a correct letter, all its occurrences in the word will be revealed!")
print("5) If you're stuck, you can type hint to get help (limited to 2 hints).")
print("\n")
print("RULES:\n")
print("• You have a limited number of attempts based on the length of the word (word length + 5 chances).")
print("• Correct guesses do not reduce your attempts.")
print("• Incorrect guesses will reduce your attempts by 1.")
print("• You can use up to 2 hints during the game by typing 'hint' when prompted.")
print("• When you use a hint, a letter will be revealed in the word automatically.")
print("• Repeating letters you've already guessed will not cost you attempts.")
print("• The game ends when:")
print("    → You successfully guess all the letters (You Win!) ")
print("    → You run out of attempts (You Lose!) \n")
print("LET'S BEGIN!")



ans='y'
while ans=='y' or ans=='yes':
    print("SELECT A CATEGORY OF WORDS TO GUESS")
    print("\n")
    print("1.\t\t\tColors")
    print("2.\t\t\tAnimals")
    print("3.\t\t\tCountries")
    print("4.\t\t\tSports")
    print("5.\t\t\tVehicles")
    print("6.\t\t\tShapes")
    print("7.\t\t\tMusical Instruments")
    print("8.\t\t\tLanguages")
    print("9.\t\t\tPlanets")
    print("10.\t\t\tOccupations")
    print("11.\t\t\tDesserts")
    print("12.\t\t\tClothing")
    print("13.\t\t\tFurniture")
    print("14.\t\t\tEmotions")
    print("15.\t\t\tGadgets")
    
    print("\n")
    print("Enter a Suitable Number of your Choice below")
    try:
        num=int(input("Enter your choice ::: "))
        while (num<1 or num>15):
            print("Enter a Valid Number\nNUMBER MUST BE BETWEEN 1 AND 15")
            num=int(input("Enter your choice ::: "))
        print("\n")
        game(num)
        print("\n")
        ans=input("Do you want to Play one more time (y/n)").lower()
    except Exception:
        print("Enter a Valid NUMBER\n")
        num=int(input("Enter your choice ::: "))
    

            

        

        

        


    