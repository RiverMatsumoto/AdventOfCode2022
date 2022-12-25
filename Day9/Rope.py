from __future__ import annotations
import numpy as np

class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
    
    def move(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def getPosition(self) -> tuple[int, int]:
        return [self.x, self.y]

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

class Rope:
    def __init__(self) -> None:
        self.head = Point()
        self.tail = Point()

    def __isTailTooFar(self) -> bool:
        tailPos = self.tail.getPosition()
        headPos = self.head.getPosition()
        xDifference = abs(headPos[0] - tailPos[0])
        yDifference = abs(headPos[1] - tailPos[1])
        return xDifference > 1 or yDifference > 1

    def __moveTail(self, position: tuple[int, int]):
        self.tail.move(position[0], position[1])

    def moveHead(self, direction: str):
        direction = direction.capitalize()
        previousPosition = self.head.getPosition()
        newX = previousPosition[0]
        newY = previousPosition[1]
        if direction == 'U':
            newY += 1
        elif direction == 'D':
            newY -= 1
        elif direction == 'L':
            newX -= 1
        elif direction == 'R':
            newX += 1
        self.head.move(newX, newY)
        
        if self.__isTailTooFar():
            self.__moveTail(previousPosition)

class LongRope:
    def __init__(self) -> None:
        self.knots = [Point() for i in range(10)]
    
    def __repr__(self) -> str:
        representation = '['
        for i in range(len(self.knots)):
            representation += str(self.knots[i])
            if i != len(self.knots) - 1:
                representation += ', '
        representation += ']'
        return representation

    def moveHead(self, direction: str):
        direction = direction.capitalize()
        previousPosition = self.knots[0].getPosition()
        newX = previousPosition[0]
        newY = previousPosition[1]
        if direction == 'U':
            newY += 1
        elif direction == 'D':
            newY -= 1
        elif direction == 'L':
            newX -= 1
        elif direction == 'R':
            newX += 1
        self.knots[0].move(newX, newY)
        
        for i in range(len(self.knots) - 1):
            head = self.knots[i].getPosition()
            tail = self.knots[i + 1].getPosition()
            xDifference = head[0] - tail[0]
            yDifference = head[1] - tail[1]
            if abs(xDifference) > 1 or abs(yDifference) > 1:
                self.knots[i + 1].move(tail[0] + np.sign(xDifference), tail[1] + np.sign(yDifference))