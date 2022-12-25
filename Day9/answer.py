from Rope import Rope
from Rope import LongRope
from Rope import Point
import matplotlib.pyplot as plt

def part1(input: list[str]):
    rope = Rope()

    tailVisited = set()
    for line in input:
        instruction = line.split()
        direction = instruction[0]
        distance = int(instruction[1])
        for i in range(distance):
            rope.moveHead(direction)
            tailPosition = rope.tail.getPosition()
            tailVisited.add((tailPosition[0], tailPosition[1]))
        
    print(f'Total points the tail visited: {len(tailVisited)}')

def part2(input: list[str]):
    rope = LongRope()

    tailVisited = set()

    for line in input:
        instruction = line.split()
        direction = instruction[0]
        distance = int(instruction[1])
        for i in range(distance):
            rope.moveHead(direction)
            tailPosition = rope.knots[-1].getPosition()
            tailVisited.add((tailPosition[0], tailPosition[1]))
    

    print(rope)
    print(f'Total positions tail visited: {len(tailVisited)}')
    xCoords = []
    yCoords = []
    for i in range(len(rope.knots)):
        xCoords.append(rope.knots[i].x)
        yCoords.append(rope.knots[i].y)

    plt.scatter(xCoords, yCoords)
    plt.grid()
    plt.show()

        
    # for line in input:
    #     instruction = line.split()
    #     direction = instruction[0]
    #     distance = int(instruction[1])
    #     for i in range(distance):
    #         rope.moveHead(direction)
        
    print(f'Total points the tail visited: {len(tailVisited)}')


with open('input.txt', 'r') as input:
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    part1(lines)
    part2(lines)