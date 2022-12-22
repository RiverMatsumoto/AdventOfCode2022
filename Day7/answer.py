from Node import Node
import numpy as np

def buildTree(input: list[str]) -> Node:
    # get rid of first cd
    input = input[1:]

    root = Node(name="/", isDirectory=True)
    current = root

    # read line
    # if it's a command "$", check if it's ls or cd
    # if it's ls, keep adding children until you reach a command
    for line in input:
        line = line.split()

        if line[0] == "$": # command
            command = line[1]
            if command == "cd": # change directory command
                directoryName = line[2]
                if directoryName == "..": # move to parent directory, else move into child directory
                    current = current.parent
                else: 
                    for child in current.children: 
                        if child.name == directoryName:
                            current = child
        elif str.isdigit(line[0]): # build tree based on ls output
            value = int(line[0])
            name = line[1]
            child = Node(name=name, value=value, isDirectory=False)
            current.AddChild(child)
        elif line[0] == "dir":
            value = 0
            name = line[1]
            child = Node(name=name, value=value, isDirectory=True)
            current.AddChild(child)
    return root


def assignValuesToDirectories(node: Node) -> int:
    if len(node.children) == 0:
        return node.value
    else:
        for child in node.children:
            node.value += assignValuesToDirectories(child)
        return node.value

def findDirectories(node: Node, total: list[int]):
    for child in node.children:
        if child.isDirectory:
            if child.value <= 100_000:
                total[0] += child.value
            findDirectories(child, total)

def findSmallestDirectoryToDelete(node: Node, minToDelete: int, candidateDirectories: list[Node]):
    for child in node.children:
        if child.isDirectory:
            if child.value >= minToDelete:
                candidateDirectories.append(child)
            findSmallestDirectoryToDelete(child, minToDelete, candidateDirectories)

def part1(input: list[str]):
    """
        Create a tree of the directories.
        Then recursively traverse through the directories and 
        find the sum of each one, base case is it's a leaf node 
        which is a file.
        Then find the directory/
    """
    root = buildTree(input)
    assignValuesToDirectories(root)
    numDirectories = [0] # can either use a global variable or mutable list to pass by reference
    findDirectories(root, numDirectories)
    print(numDirectories)

def part2(input: list[str]):
    root = buildTree(input)
    assignValuesToDirectories(root)

    totalSpace = 70_000_000
    freeSpaceNeeded = 30_000_000
    spaceTakenUp = root.value
    currentFreeSpace = totalSpace - spaceTakenUp
    minNeededToDelete = freeSpaceNeeded - currentFreeSpace
    candidateDirectories = []

    findSmallestDirectoryToDelete(root, minToDelete=minNeededToDelete, candidateDirectories=candidateDirectories)
    names = []
    values = []
    for node in candidateDirectories:
        names.append(node.name)
        values.append(node.value)
    
    sortedValues = values.copy()
    sortedValues.sort()
    print(f'Sorted: {sortedValues[:5]}')
    # print(f'All candidate directories to delete: {candidateDirectories}')
    print(f'Total space on system = 70_000_000')
    print(f'Space required = 30_000_000')
    print(f'Space taken up = {spaceTakenUp}')
    print(f'Current free space = {currentFreeSpace}')
    print(f'Minimum space to delete for update = {minNeededToDelete}')
    print(f'Minimum size directory to delete to get required space: {values[np.argmin(values)]}. Name: {names[np.argmin(values)]}')


with open('input.txt', 'r') as input:
    lines = input.readlines()
    part1(lines)
    part2(lines)