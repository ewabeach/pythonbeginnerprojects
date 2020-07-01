import random
randomnumber = random.randint(1, 100)
lives = 10

def main():
    while True:
        maininput = int(input(">>>"))
        if maininput > randomnumber:
            global lives
            lives -= 1
            print("======================================================================================================")
            print("You guessed too high. You have %s lives remaining." % (lives))
            print("======================================================================================================")
        elif maininput < randomnumber:
            lives -= 1
            print("======================================================================================================")
            print("You guessed too low. You have %s lives remaining." % (lives))
            print("======================================================================================================")
        elif maininput == randomnumber:
            print("======================================================================================================")
            print("You successfully guessed the number with %s lives remaining, congratulations!" % (lives)) 
            print("======================================================================================================")
            break
        if lives == 0:
            print("======================================================================================================")
            print("You lost the game. The number was %i. Better luck next time!" % (randomnumber))
            print("======================================================================================================")
            break
        
def rules():
    print("======================================================================================================")
    print("The objective of the game is to guess the computer's randomly generated number within %i tries." % (lives))
    print("If you guess the number before you run out of tries you win.")
    print("However if you don't guess the number and run out of tries you lose.")
    print("The computer will generate a number from 1 - 100. Type go to continue to the game.")
    print("======================================================================================================")

print("======================================================================================================")
print("This is Justin's Random Number Game.")
print("If you know how to play then type 'go'. ")
print("If you don't know how to play then type 'rules'. ")
print("======================================================================================================")
userinput = input(">>>")

if userinput == "rules":
    rules()
    userinput = input(">>>")
    if userinput == "go":
        print("======================================================================================================")
        print("The computer has chose its number. This is your first guess and you have %i lives remaining." % (lives))
        print("======================================================================================================")
        main()
elif userinput == "go":
    print("======================================================================================================")
    print("The computer has chose its number. This is your first guess and you have %i lives remaining." % (lives))
    print("======================================================================================================")
    main()