#The guessing game using classes, functions, and conditional statements

import random
i = 0
wins = 0
loss = 0
# x = random.randint(1, 10)
# print(x)
# val = input("Guess a number: ")
# newval = int(val)
# print(newval)

class Person:
    def __init__(self, name, age, country, race, occupation, playGame):
        self.name = name
        self.age = age
        self.country = country
        self.race = race
        self.occupation = occupation
        self.playGame = playGame

    def aboutMe(self):
        print("Your name is " + self.name + ", You are " + str(self.age) + " years old." + " You are from " + self.country + ". You are "
              + self.race + ", and You are a/an " + self.occupation + ". You answered " + self.playGame + " to play the guessing game.")


#User inputs to start the game
r1 = input("What is your name?: ")
r2 = input("How old are you?: ")
r3 = input("Where are you from?: ")
r4 = input("What race are you?: ")
r5 = input("What is your occupation?: ")
r6 = input("Do you want to play a guessing game?(y/n):  ")

print("")

p1 = Person(r1, r2, r3, r4, r5, r6)
p1.aboutMe()


# Setting up the game. initialize the wins and loss count

#myChoice()
def initiateGame():
    if r6 == 'y':
        print("This game is fairly easy, you only need to guess a number between 1 and 10. If your guessed number "
              "matches the randomly picked number, you win. Good luck!")

        def myChoice():
            i = 0
            wins = 0
            loss = 0
        # While i is less than 10 because i want the game to have 10 runs
            while i < 10:
                # print(i)
                x = random.randint(1, 10)
                val = input("Guess a number: ")
                newval = int(val)
                print(newval)
                if newval == x:
                    print("You guessed right")
                    wins += 1
                    # print(wins)
                else:
                    print("You guessed wrong, try again")
                    loss += 1
                    # print(loss)
                i += 1
            print("Wins: " + str(wins))
            print("Loss: " + str(loss))
        myChoice()


    else:
        print("You have chosen not to play the game. Good bye.")


initiateGame()



