# Part 1
def find_overlaps(filename='input.txt'):
    sections = []
    with open(filename, 'r') as f:
        for line in f:
            [elf1, elf2] = line.split(",")
            elf1_boundaries = [int(n) for n in elf1.split("-")]
            elf2_boundaries = [int(n) for n in elf2.split("-")]
            elf1_sections = list(range(elf1_boundaries[0], elf1_boundaries[1]+1))
            elf2_sections = list(range(elf2_boundaries[0], elf2_boundaries[1]+1))
            sections.append((elf1_sections, elf2_sections))

    total_overlap_counter = 0
    for elf1,elf2 in sections:
        overlap = [value for value in elf1 if value in elf2]
        if overlap == elf1 or overlap == elf2:
            total_overlap_counter += 1

    return total_overlap_counter

print(find_overlaps('input.txt'))