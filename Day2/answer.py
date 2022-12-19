import numpy as np

def getOptionScore(myOption: str) -> int:
    if (myOption == "rock"):
        return 1
    elif (myOption == "paper"):
        return 2
    elif (myOption == "scissors"):
        return 3

def getOutcomeScore(opponent: str, me: str) -> int:
    if opponent == "rock":
        if me == "rock":
            return 3
        if me == "paper":
            return 6
        if me == "scissors":
            return 0
    if opponent == "paper":
        if me == "rock":
            return 0
        if me == "paper":
            return 3
        if me == "scissors":
            return 6
    if opponent == "scissors":
        if me == "rock":
            return 6
        if me == "paper":
            return 0
        if me == "scissors":
            return 3

def part1():
    with open("input.txt", "r") as input:
        rpsGames = input.readlines()
        totalScore = 0

        for game in rpsGames:
            opponent = game[0]
            me = game[2]
            if (opponent == "A"):
                opponent = "rock"
            if (opponent == "B"):
                opponent = "paper"
            if (opponent == "C"):
                opponent = "scissors"
            if (me == "X"):
                me = "rock"
            if (me == "Y"):
                me = "paper"
            if (me == "Z"):
                me = "scissors"
            totalScore += getOptionScore(me)
            totalScore += getOutcomeScore(opponent=opponent, me=me)
            
        print(totalScore)

def calculateDesiredOutcome(opponent: str, desiredOutcome: str) -> str:
    if opponent == "rock":
        if desiredOutcome == "lose":
            return "scissors"
        if desiredOutcome == "draw":
            return "rock"
        if desiredOutcome == "win":
            return "paper"
    if opponent == "paper":
        if desiredOutcome == "lose":
            return "rock"
        if desiredOutcome == "draw":
            return "paper"
        if desiredOutcome == "win":
            return "scissors"
    if opponent == "scissors":
        if desiredOutcome == "lose":
            return "paper"
        if desiredOutcome == "draw":
            return "scissors"
        if desiredOutcome == "win":
            return "rock"

def part2():
    with open("input.txt", "r") as input:
        rpsGames = input.readlines()
        totalScore = 0

        for game in rpsGames:
            opponent = game[0]
            desiredOutcome = game[2]
            if (opponent == "A"):
                opponent = "rock"
            if (opponent == "B"):
                opponent = "paper"
            if (opponent == "C"):
                opponent = "scissors"
            if desiredOutcome == "X":
                desiredOutcome = "lose"
            if desiredOutcome == "Y":
                desiredOutcome = "draw"
            if desiredOutcome == "Z":
                desiredOutcome = "win"
            me = calculateDesiredOutcome(opponent=opponent, desiredOutcome=desiredOutcome)
            totalScore += getOptionScore(me) + getOutcomeScore(opponent=opponent, me=me)
        
        print(totalScore)


    

if __name__ == "__main__":
    part1()
    part2()
