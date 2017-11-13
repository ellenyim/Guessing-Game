import random

def main():
    guess1 = 0
    guess2 = 0
    guess3 = 0
    guess4 = 0

    print("Welcome to my Guessing Game! ")
    print("Now you get to choose 3 levels, Easy, Medium, Hard. ")
    print("1. Easy(10)  2. Medium(20)   3. Hard(100)    ")
    level = input("Choose what level you would like to play: ")

#easy
    if level == 1:
        print("Great. Grab a friend and let's get started. ")
        print("First one to get the correct number wins. ")
        print("1-10")
        print("Round 1")
        ans = random.randrange(1, 11)
        while guess1 < 10:
            guess1 = guess1 + 1
            num4 = input("Player One - Enter a number between 1 and 10: ")
            if num4 < ans:
                print("Higher")
            if num4 > ans:
                print("Lower")
            if num4 == ans:
                break
        if guess1 < 10:
            print("You got the correct number. ")
        if guess1 > 10:
            print("Sorry, you didn't get the correct number.")

        ans = random.randrange(1, 11)
        while guess2 < 10:
            guess2 = guess2 + 1
            num5 = input("Player Two - Enter a number between 1 and 10: ")
            if num5 < ans:
                print("Higher")
            if num5 > ans:
                print("Lower")
            if num5 == ans:
                break
        if guess2 < 10:
            print("You got the correct number. ")
        if guess2 > 10:
            print("Sorry, You didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")

        print("Round 2. ")
        ans = random.randrange(1, 11)
        while guess1 < 10:
            guess1 = guess1 + 1
            num4 = input("Player One - Enter a number between 1 and 10: ")
            if num4 < ans:
                print("Higher")
            if num4 > ans:
                print("Lower")
            if num4 == ans:
                break
        if guess1 < 10:
            print("You got the correct number. ")
        if guess1 > 10:
            print("Sorry, you didn't get the correct number.")

        ans = random.randrange(1, 11)
        while guess2 < 10:
            guess2 = guess2 + 1
            num5 = input("Player Two - Enter a number between 1 and 10: ")
            if num5 < ans:
                print("Higher")
            if num5 > ans:
                print("Lower")
            if num5 == ans:
                break
        if guess2 < 10:
            print("You got the correct number. ")
        if guess2 > 10:
            print("Sorry, You didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")

        print("Round 3.")
        ans = random.randrange(1, 11)
        while guess1 < 10:
            guess1 = guess1 + 1
            num4 = input("Player One - Enter a number between 1 and 10: ")
            if num4 < ans:
                print("Higher")
            if num4 > ans:
                print("Lower")
            if num4 == ans:
                break
        if guess1 < 10:
            print("You got the correct number. ")
        if guess1 > 10:
            print("Sorry, you didn't get the correct number.")

        ans = random.randrange(1, 11)
        while guess2 < 10:
            guess2 = guess2 + 1
            num5 = input("Player Two - Enter a number between 1 and 10: ")
            if num5 < ans:
                print("Higher")
            if num5 > ans:
                print("Lower")
            if num5 == ans:
                break
        if guess2 < 10:
            print("You got the correct number. ")
        if guess2 > 10:
            print("Sorry, You didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")
#Determining the winner of all 3 rounds.
#if player one wins
        if guess1 < guess2:  # 1
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2:  # 2
            if guess1 < guess2:
                if guess1 > guess2:
                    print("Player One Wins. ")
        if guess1 > guess2:  # 3
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2:  # 4
            if guess1 > guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 == guess2:  # 5
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2:  # 6
            if guess1 == guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2:  # 7
            if guess1 < guess2:
                if guess1 == guess2:
                    print("Player One Wins. ")

# if player two wins.
        if guess1 > guess2:  # 1
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2:  # 2
            if guess1 > guess2:
                if guess1 < guess2:
                    print("Player Two Wins. ")
        if guess1 < guess2:  # 3
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2:  # 4
            if guess1 < guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 == guess2:  # 5
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2:  # 6
            if guess1 == guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2:  # 7
            if guess1 > guess2:
                if guess1 == guess2:
                    print("Player Two Wins. ")

# IF it's a TIE.
        if guess1 > guess2:  # 1
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 2
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 3
            if guess1 < guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 4
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 > guess2:  # 5
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE. ")
        if guess1 == guess2:  # 6
            if guess1 > guess2:
                if guess1 < guess2:
                    print("TIE.")
        if guess1 == guess2:  # 7
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE. ")
        if guess1 == guess2:  # 8
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 9
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 > guess2:  # 10
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 11
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 12
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 13
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE")


#medium
    elif level == 2:
        print("Great. Let's get started. ")
        print("First one to get the correct number wins. ")
        print("1-20.")
        print("Round 1")
        num3 = random.randrange(1, 21)
        while guess3 < 15:
            guess3 = guess3 + 1
            num = input("Player One, choose a # between 1-20.")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess3 < 15:
            print("You got the correct number. ")
        if guess3 > 15:
            print("Sorry, You didn't get the correct number. ")

        num3 = random.randrange(1, 21)
        while guess4 < 15:
            guess4 = guess4 + 1
            num = input("Player Two, Choose a # between 1-20. ")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess4 < 15:
            print("You got the correct number. ")
        if guess4 > 15:
            print("Sorry, you didn't get the correct number.")

        if guess3 == guess4:
            print("Tie")
        if guess3 < guess4:
            print("Player One Wins.")
        if guess3 > guess4:
            print("Player Two Wins.")

        print("Round 2. ")
        num3 = random.randrange(1, 21)
        while guess3 < 15:
            guess3 = guess3 + 1
            num = input("Player One, choose a # between 1-20.")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess3 < 15:
            print("You got the correct number. ")
        if guess3 > 15:
            print("Sorry, You didn't get the correct number. ")

        num3 = random.randrange(1, 21)
        while guess4 < 15:
            guess4 = guess4 + 1
            num = input("Player Two, Choose a # between 1-20. ")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess4 < 15:
            print("You got the correct number. ")
        if guess4 > 15:
            print("Sorry, you didn't get the correct number.")

        if guess3 == guess4:
            print("Tie")
        if guess3 < guess4:
            print("Player One Wins.")
        if guess3 > guess4:
            print("Player Two Wins.")

        print("Round 3")
        num3 = random.randrange(1, 21)
        while guess3 < 15:
            guess3 = guess3 + 1
            num = input("Player One, choose a # between 1-20.")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess3 < 15:
            print("You got the correct number. ")
        if guess3 > 15:
            print("Sorry, You didn't get the correct number. ")

        num3 = random.randrange(1, 21)
        while guess4 < 15:
            guess4 = guess4 + 1
            num = input("Player Two, Choose a # between 1-20. ")
            if num < num3:
                print("Higher")
            if num > num3:
                print("Lower")
            if num == num3:
                break
        if guess4 < 15:
            print("You got the correct number. ")
        if guess4 > 15:
            print("Sorry, you didn't get the correct number.")

        if guess3 == guess4:
            print("Tie")
        if guess3 < guess4:
            print("Player One Wins.")
        if guess3 > guess4:
            print("Player Two Wins.")
#determining the winner for all 3 rounds.
#if player one wins
        if guess3 < guess4:  # 1
            if guess3 < guess4:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess3 < guess4:  # 2
            if guess3 < guess4:
                if guess1 > guess2:
                    print("Player One Wins. ")
        if guess3 > guess4:  # 3
            if guess3 < guess4:
                if guess3 < guess4:
                    print("Player One Wins. ")
        if guess3 < guess4:  # 4
            if guess3 > guess4:
                if guess3 < guess4:
                    print("Player One Wins. ")
        if guess3 == guess4:  # 5
            if guess3 < guess4:
                if guess3 < guess4:
                    print("Player One Wins. ")
        if guess3 < guess4:  # 6
            if guess3 == guess4:
                if guess3 < guess4:
                    print("Player One Wins. ")
        if guess3 < guess4:  # 7
            if guess3 < guess4:
                if guess3 == guess3:
                    print("Player One Wins. ")

# if player two wins.
        if guess3 > guess4:  # 1
            if guess3 > guess4:
                if guess3 > guess4:
                    print("Player Two Wins. ")
        if guess3 > guess4:  # 2
            if guess3 > guess4:
                if guess3 < guess4:
                    print("Player Two Wins. ")
        if guess3 < guess4:  # 3
            if guess3 > guess4:
                if guess3 > guess4:
                    print("Player Two Wins. ")
        if guess3 > guess4:  # 4
            if guess3 < guess4:
                if guess3 > guess4:
                    print("Player Two Wins. ")
        if guess3 == guess4:  # 5
            if guess3 > guess4:
                if guess3 > guess4:
                    print("Player Two Wins. ")
        if guess3 > guess4:  # 6
            if guess3 == guess4:
                if guess3 > guess4:
                    print("Player Two Wins. ")
        if guess3 > guess4:  # 7
            if guess3 > guess4:
                if guess3 == guess4:
                    print("Player Two Wins. ")

#Tie.
        if guess1 > guess2:  # 1
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 2
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 3
            if guess1 < guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 4
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 > guess2:  # 5
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE. ")
        if guess1 == guess2:  # 6
            if guess1 > guess2:
                if guess1 < guess2:
                    print("TIE.")
        if guess1 == guess2:  # 7
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE. ")
        if guess1 == guess2:  # 8
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2:  # 9
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 > guess2:  # 10
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 11
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 12
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2:  # 13
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE")

#hard
    if level == 3:
        print("Great. Let's get started. ")
        print("First one to get the correct number wins. ")
        print("1-100.")
        print("Round 1")
        num4 = random.randrange(1, 101)
        while guess1 < 30:
            guess1 = guess1 + 1
            num = input("Player One, choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess1 < 30:
            print("You got the correct number.")
        if guess1 > 30:
            print("Sorry, you didn't get the correct number. ")

        num4 = random.randrange(1, 101)
        while guess2 < 30:
            guess2 = guess2 + 1
            num = input("Player Two, Choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess2 < 30:
            print("You got the correct number. ")
        if guess2 > 30:
            print("Sorry, you didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")

        print("Round 2")
        print("1-100.")
        num4 = random.randrange(1, 101)
        while guess1 < 30:
            guess1 = guess1 + 1
            num = input("Player One, choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess1 < 30:
            print("You got the correct number.")
        if guess1 > 30:
            print("Sorry, you didn't get the correct number. ")

        num4 = random.randrange(1, 101)
        while guess2 < 30:
            guess2 = guess2 + 1
            num = input("Player Two, Choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess2 < 30:
            print("You got the correct number. ")
        if guess2 > 30:
            print("Sorry, you didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")

        print("Round 3.")
        print("1-100.")
        num4 = random.randrange(1, 101)
        while guess1 < 30:
            guess1 = guess1 + 1
            num = input("Player One, choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess1 < 30:
            print("You got the correct number.")
        if guess1 > 30:
            print("Sorry, you didn't get the correct number. ")

        num4 = random.randrange(1, 101)
        while guess2 < 30:
            guess2 = guess2 + 1
            num = input("Player Two, Choose a number between 1 and 100. ")
            if num < num4:
                print("Higher")
            if num > num4:
                print("Lower")
            if num == num4:
                break
        if guess2 < 30:
            print("You got the correct number. ")
        if guess2 > 30:
            print("Sorry, you didn't get the correct number. ")

        if guess1 == guess2:
            print("Tie")
        if guess1 < guess2:
            print("Player One Wins.")
        if guess1 > guess2:
            print("Player Two Wins.")
#determining the winner for all 3 rounds, hard
#if Player One wins.
        if guess1 < guess2: #1
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2: #2
            if guess1 < guess2:
                if guess1 > guess2:
                    print("Player One Wins. ")
        if guess1 > guess2: #3
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2: #4
            if guess1 > guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 == guess2: #5
            if guess1 < guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2: #6
            if guess1 == guess2:
                if guess1 < guess2:
                    print("Player One Wins. ")
        if guess1 < guess2:#7
            if guess1 < guess2:
                if guess1 == guess2:
                    print("Player One Wins. ")

#if player two wins.
        if guess1 > guess2: #1
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2: #2
            if guess1 > guess2:
                 if guess1 < guess2:
                     print("Player Two Wins. ")
        if guess1 < guess2: #3
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2: #4
            if guess1 < guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 == guess2: #5
            if guess1 > guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2: #6
            if guess1 == guess2:
                if guess1 > guess2:
                    print("Player Two Wins. ")
        if guess1 > guess2: #7
            if guess1 > guess2:
                if guess1 == guess2:
                    print("Player Two Wins. ")

#IF it's a TIE.
        if guess1 > guess2: #1
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2: #2
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2: #3
            if guess1 < guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 < guess2: #4
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE. ")
        if guess1 > guess2: #5
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE. ")
        if guess1 == guess2: #6
            if guess1 > guess2:
                if guess1 < guess2:
                    print("TIE.")
        if guess1 == guess2: #7
            if guess1 == guess2:
                    if guess1 == guess2:
                        print("TIE. ")
        if guess1 == guess2: #8
            if guess1 == guess2:
                if guess1 < guess2:
                    print("TIE. ")
        if guess1 < guess2: #9
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 > guess2: #10
            if guess1 == guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2: #11
            if guess1 < guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2: #12
            if guess1 > guess2:
                if guess1 == guess2:
                    print("TIE")
        if guess1 == guess2: #13
            if guess1 == guess2:
                if guess1 > guess2:
                    print("TIE")

main()

def play_again():
    while True:
        print("1. Yes       2. No")
        play_again = input("Would you like to play again (Yes or No): ")
        if play_again == 1:
            main()
        if play_again == 2:
            exit()
        else:
            print("Couldn't recognize what you entered. ")
play_again()
