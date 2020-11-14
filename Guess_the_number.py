import random


# function ask about number until user choose proper number
def guess_the_number():
    try:
        drawed_number = random.randint(1, 100)
        while True:
            user_number = int(input("Guess the number: "))
            if user_number > drawed_number:
                print("Too Big!")
            elif user_number < drawed_number:
                print("Too small!")
            elif user_number == drawed_number:
                print("You win!!!")
                break
    except ValueError:
        print("It's not a number")
    return


guess_the_number()
