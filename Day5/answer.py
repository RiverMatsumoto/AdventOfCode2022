import numpy as np

def executeStep(stacks, numCrates, fromStack, toStack) -> None:
    for i in range(0, numCrates):
        stacks[toStack].append(stacks[fromStack].pop())

def executeStepPart2(stacks, numCrates, fromStack, toStack) -> None:
    tempStack = []
    for i in range(numCrates):
        tempStack.append(stacks[fromStack].pop())
    for i in range(len(tempStack)):
        stacks[toStack].append(tempStack.pop())

stack1 =  ["N", "B", "D", "T", "V", "G", "Z", "J"]
stack2 =  ["S", "R", "M", "D", "W", "P", "F"]
stack3 =  ["V", "C", "R", "S", "Z"]
stack4 =  ["R", "T", "J", "Z", "P", "H", "G"]
stack5 =  ["T", "C", "J", "N", "D", "Z", "Q", "F"]
stack6 =  ["N", "V", "P", "W", "G", "S", "F", "M"]
stack7 =  ["G", "C", "V", "B", "P", "Q"]
stack8 =  ["Z", "B", "P", "N"]
stack9 =  ["W", "P", "J"]
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

print(stacks)

with open("input.txt", "r") as input:
    steps = input.readlines()

    for step in steps:
        if (step[0] != "m"):
            continue
        words = step.split()
        numCrates = int(words[1]) 
        fromStack = int(words[3]) - 1 # minus 1 for index
        toStack = int(words[5]) - 1
        executeStepPart2(stacks, numCrates, fromStack, toStack)
    
    

for stack in stacks:
    print(stack[-1])



