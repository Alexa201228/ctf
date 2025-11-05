from collections import Counter


def count_relevant_lines(filename: str) -> int:
    counter = 0
    with open(filename, "rt") as f:
        for line in f.readlines():
            count_dict = Counter(line)
            if count_dict['0'] % 3 == 0 or count_dict['1'] % 2 == 0:
                counter += 1
    
    print(counter)


count_relevant_lines("data.dat")
