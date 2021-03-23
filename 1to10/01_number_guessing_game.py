# DomirScire
import random

def guessting_game():
    count=0
    randNum = random.randint(0,100)
    while True:
        u_input = input("Guess the Number: ")
        u_input = int(u_input)
        if u_input == randNum:
            print('Just Right')
            break
        elif u_input > randNum:
            print("Too High")
            count += 1
        elif u_input < randNum:
            print("Too Low")
            count += 1
        if count == 3:
            break

if __name__ == "__main__":
    guessting_game()
