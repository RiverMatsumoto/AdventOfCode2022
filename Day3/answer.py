
def asciiToPriority(item: int) -> int:
    if item >= 65 and item <= 90:
        return item - 38
    elif item >= 97 and item <= 122:
        return item - 96
    else:
        return 0

def part1(bags: list[str]) -> None:
    sum = 0
    for bag in bags:
        halfIndex = len(bag) // 2
        leftHalf = bag[:halfIndex]
        rightHalf = bag[halfIndex:]

        leftHalf = set(leftHalf)
        rightHalf = set(rightHalf)

        # find common item
        commonItems = leftHalf.intersection(rightHalf)
        
        # must loop over the set, can't index into it
        for item in commonItems:
            sum += asciiToPriority(ord(item))
    print(f"Part 1 sum: {sum}")

def part2(bags: list[str]) -> None:
    sum = 0

    # find a triple intersection, A subset B and B subset C
    # iterate through each group
    for firstElfEachGroup in range(0, len(bags), 3):
        elf1 = set(bags[firstElfEachGroup])
        elf2 = set(bags[firstElfEachGroup + 1])
        elf3 = set(bags[firstElfEachGroup + 2])

        # clean out newlines
        elf1.discard("\n")
        elf2.discard("\n")
        elf3.discard("\n")
        
        # by transitive property of set intersection, A subset of B and B subset of C means A subset C
        elf1SubsetOfElf2 = elf1.intersection(elf2)
        commonItems = elf1SubsetOfElf2.intersection(elf3)

        for item in commonItems:
            print(f"item = {item} = {ord(item)}, priority = {asciiToPriority(ord(item))}")
            sum += asciiToPriority(ord(item))
    print(f"Part 2 answer: {sum}")


with open("input.txt", "r") as input:
    bags = input.readlines()
    part1(bags)
    part2(bags)

with open("test.txt", "r") as input:
    bags = input.readlines()
    # part2(bags)
