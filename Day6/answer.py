def hasDuplicates(lastFour: str) -> bool:
    lastFourSet = set(lastFour)
    return len(lastFour) != len(lastFourSet)

def generalSolution(packet: str, numDistinctChars: int):
    numCharactersUntilStart = numDistinctChars
    lastNChars = packet[:numDistinctChars]
    packet = packet[numDistinctChars:]
    
    for char in packet:
        if hasDuplicates(lastNChars):
            lastNChars = lastNChars[1:] + char
            numCharactersUntilStart += 1
        else:
            break
    
    print(f'Number of characters until start-of-packet marker with {numDistinctChars} distinct characters: {numCharactersUntilStart}')

with open('input.txt', 'r') as input:
    packet = input.readline()[:-1]
    generalSolution(packet, 4)
    generalSolution(packet, 14)
