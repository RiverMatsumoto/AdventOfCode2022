def isFullyOverlapping(elf1: tuple[int, int], elf2: tuple[int, int]) -> bool:
    lMin = elf1[0]
    lMax = elf1[1]
    rMin = elf2[0]
    rMax = elf2[1]

    if lMin >= rMin and lMax <= rMax:
        return True
    elif rMin >= lMin and rMax <= lMax:
        return True
    else:
        return False

def isOverlapping(elf1: tuple[int, int], elf2: tuple[int, int]) -> bool:
    lMin = elf1[0]
    lMax = elf1[1]
    rMin = elf2[0]
    rMax = elf2[1]

    if lMin <= rMax and lMax >= rMin:
        return True
    else:
        return False

def part1(input: list[str]) -> None:
    totalContainingRanges = 0

    for line in input:
        # get rid of new line character
        line = line[:-1]
        
        # parse the number ranges and store them as tuples
        elves = line.split(",")
        elf1 = filter(str.isdigit, elves[0].partition("-"))
        elf2 = filter(str.isdigit, elves[1].partition("-"))
        
        # convert from strings to integers
        elf1 = tuple(map(lambda item: int(item), elf1))
        elf2 = tuple(map(lambda item: int(item), elf2))

        if isFullyOverlapping(elf1, elf2):
            totalContainingRanges += 1
    print(f'Part 1: {totalContainingRanges}')

# same as part 1 but different check
def part2(input: list[str]) -> None:
    totalContainingRanges = 0

    for line in input:
        # get rid of new line character
        line = line[:-1]
        
        # parse the number ranges and store them as tuples
        elves = line.split(",")
        elf1 = filter(str.isdigit, elves[0].partition("-"))
        elf2 = filter(str.isdigit, elves[1].partition("-"))
        
        # convert from strings to integers
        elf1 = tuple(map(lambda item: int(item), elf1)) 
        elf2 = tuple(map(lambda item: int(item), elf2))

        if isOverlapping(elf1, elf2):
            totalContainingRanges += 1
    print(f'Part 2: {totalContainingRanges}')


with open("input.txt", "r") as input:
    lines = input.readlines()
    part1(lines)
    part2(lines)