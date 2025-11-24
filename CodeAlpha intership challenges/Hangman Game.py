import random
wordbank = ['roots', 'plant', 'state', 'india']
word = list(random.choice(wordbank))
flag = True
while flag: 
    lives = 5
    answer = ["_" for i in range(len(word))]
    print("Guess the following word by substituting letters: ")
    for i in answer:
        print(i, end = " ")
    print()
    for i in range(lives):
        if "".join(answer) != "".join(word):
            guess_letter = input("Enter a letter: ").lower()
            for index, letter in enumerate(word):
                if guess_letter == letter:
                    answer[index] = guess_letter
            for i in answer:
                print(i, end = " ")
            lives = lives-1
            print(f"You have {lives} left")
        else:
            break
    if "".join(answer) == "".join(word):
        print("You won!")
    else:
        print("You lost")
    again = input("Do you want to  play again? (y/n): ").lower()
    if again == "y":
        flag = True
    else:
        print("Thankyou for playing with us!")
        flag = False