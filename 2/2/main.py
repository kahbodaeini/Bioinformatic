def assessing_assembly_quality(strings, N):

    lens = [len(string) for string in strings]
    lens.sort()
    summation = 0
    for string in lens:
        summation += string
    num = N * summation / 100
    count = 0
    size = len(lens)
    while count < num:
        count += lens[size - 1]
        size -= 1
    return lens[size]


f = open("input.txt", 'r')
strings = f.read().splitlines()

N_50 = assessing_assembly_quality(strings, 50)
N_75 = assessing_assembly_quality(strings, 75)

output = open("output.txt", 'w')
output.write(f"{N_50} {N_75}")
