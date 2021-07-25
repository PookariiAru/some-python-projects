import itertools
alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
f = open("dict1.txt", "w")
for passlen in [5]:
    combinations = itertools.product(alphabets, repeat = passlen)
    for combination in combinations:
        f.write(''.join(combination)+"\n")
