import util

def get_common_items(p1,p2):
    s1 = set([c for c in p1])
    s2 = set([c for c in p2])
    return s1.intersection(s2)

def get_commons_items_part2(p1,p2,p3):
    s1 = set([c for c in p1])
    s2 = set([c for c in p2])
    s3 = set([c for c in p3])
    return s1.intersection(s2).intersection(s3)

def get_total_priority():
    input_lines = util.read_input(day=3)
    priority = 0
    for input in input_lines:
        l = len(input)
        common_items = get_common_items(input[:l//2] , input[l//2:])
        for common in common_items:
            if common.islower():
                priority = priority + ord(common) - ord('a') + 1
            else:
                priority = priority + ord(common) - ord('A') + 27

    return priority


def get_total_priority_by_groups():
    input_lines = util.read_input(day=3)
    priority = 0
    l = len(input_lines)
    groups = [ [input_lines[i], input_lines[i+1], input_lines[i+2]] for i in range(0,l,3) ]
    for group in groups:
        common = get_commons_items_part2(group[0].strip('\n'),group[1].strip('\n'), group[2].strip('\n'))
        for c in common:
            if c.islower():
                priority = priority + ord(c) - ord('a') + 1
            else:
                priority = priority + ord(c) - ord('A') + 27

    return priority


print(get_total_priority_by_groups())


