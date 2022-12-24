import numpy as np

def part1(input: list[str]):
    # build tree grid 
    treeGrid = []
    rowIndex = 0
    for row in input:
        treeGrid.append([])
        for treeHeight in row:
            treeGrid[rowIndex].append(int(treeHeight))
        rowIndex += 1
        
    # Shoot a "laser" through each edge while keeping track of the seen or visible trees
    treesPerRow = len(treeGrid[0])
    treesPerCol = len(treeGrid)
    visibleTreeSet = set()
    visibleTrees = 0

    # top side
    for col in range(treesPerRow):
        currentTallest = -1
        for row in range(treesPerCol):
            currentTree = treeGrid[row][col]
            if currentTree > currentTallest:
                currentTallest = currentTree
                if (row, col) not in visibleTreeSet:
                    visibleTreeSet.add((row, col))
                    visibleTrees += 1
    
    # bottom side
    for col in range(treesPerRow):
        currentTallest = -1
        for row in range(treesPerCol - 1, -1, -1):
            currentTree = treeGrid[row][col]
            if currentTree > currentTallest:
                currentTallest = currentTree
                if (row, col) not in visibleTreeSet:
                    visibleTreeSet.add((row, col))
                    visibleTrees += 1

    # left side
    for row in range(treesPerCol):
        currentTallest = -1
        for col in range(treesPerRow):
            currentTree = treeGrid[row][col]
            if currentTree > currentTallest:
                currentTallest = currentTree
                if (row, col) not in visibleTreeSet:
                    visibleTreeSet.add((row, col))
                    visibleTrees += 1
    
    # right side
    for row in range(treesPerCol):
        currentTallest = -1
        for col in range(treesPerRow - 1, -1, -1): # move from right to left side
            currentTree = treeGrid[row][col]
            if currentTree > currentTallest:
                currentTallest = currentTree
                if (row, col) not in visibleTreeSet:
                    visibleTreeSet.add((row, col))
                    visibleTrees += 1

    print(visibleTrees)

def outOfBounds(pointer: list[int], treeGrid: list[list[int]]):
    maxCol = len(treeGrid[0]) - 1
    maxRow = len(treeGrid) - 1
    if pointer[0] > maxRow or pointer[0] < 0:
        return True
    elif pointer[1] > maxCol or pointer[1] < 0:
        return True
    return False

def calculateVisibilityScore(treeGrid: list[list[int]], coord: list[int]) -> int:
    treeHeight = treeGrid[coord[0]][coord[1]]
    visibleUp = 0
    visibleDown = 0
    visibleLeft = 0
    visibleRight = 0

    # check up
    pointer = coord.copy()
    while True:
        pointer[0] -= 1
        if outOfBounds(pointer, treeGrid): 
            break
        if treeGrid[pointer[0]][pointer[1]] >= treeHeight:
            visibleUp += 1
            break
        visibleUp += 1

    # check down
    pointer = coord.copy()
    while True:
        pointer[0] += 1
        if outOfBounds(pointer, treeGrid): 
            break
        if treeGrid[pointer[0]][pointer[1]] >= treeHeight:
            visibleDown += 1
            break
        visibleDown += 1

    # check left
    pointer = coord.copy()
    while True:
        pointer[1] -= 1
        if outOfBounds(pointer, treeGrid): 
            break
        elif treeGrid[pointer[0]][pointer[1]] >= treeHeight:
            visibleLeft += 1
            break
        else:
            visibleLeft += 1

    # check right
    pointer = coord.copy()
    while True:
        pointer[1] += 1
        if outOfBounds(pointer, treeGrid): 
            break
        if treeGrid[pointer[0]][pointer[1]] >= treeHeight:
            visibleRight += 1
            break
        visibleRight += 1

    return visibleUp * visibleDown * visibleLeft * visibleRight

def part2(input: list[str]):
    # iterate through each internal tree (not edges) and 
    # get the number of visible trees in each direction
    # keep list of scores and take the highest one

    # build tree grid 
    treeGrid = []
    rowIndex = 0
    for row in input:
        treeGrid.append([])
        for treeHeight in row:
            treeGrid[rowIndex].append(int(treeHeight))
        rowIndex += 1

    # only calculate scores for internal trees
    treesPerRow = range(1, len(treeGrid[0]) - 1)
    treesPerCol = range(1, len(treeGrid) - 1)
    print(*treesPerRow)
    print(*treesPerCol)

    visibilityScores = []
    for row in treesPerCol:
        for col in treesPerRow:
            visibilityScores.append(calculateVisibilityScore(treeGrid, [row, col]))
    print(f'Part 2: {np.max(visibilityScores)}')


with open('input.txt', 'r') as input:
    treeGrid = input.readlines()
    for i in range(len(treeGrid)):
        treeGrid[i] = treeGrid[i][:-1]
    part1(treeGrid)
    part2(treeGrid)