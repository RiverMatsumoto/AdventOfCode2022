import numpy as np

with open("input.txt", "r") as input:
    data = input.readlines()
    elvesCal = []
    currentElfCal = 0
    for line in data:
        if (line == "\n"):
            elvesCal.append(currentElfCal)
            currentElfCal = 0
        else:
            currentElfCal += int(line[:-1])
    sored = np.sort(elvesCal)
    sored = np.flip(sored)
    print(sored[:3])
    print(sored[:10])
    sum = 0
    for num in sored[:3]:
        sum += num
    print(sum)

