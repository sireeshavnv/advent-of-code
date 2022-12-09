import util

def get_complete_overlaps():
    input_lines = util.read_input(day=4)
    assignments =  [pair.strip("\n").split(",") for pair in input_lines]
    overlaps = 0
    for assignment_pair in assignments:
        s1, e1 = int(assignment_pair[0].split("-")[0]), int(assignment_pair[0].split("-")[1])
        s2, e2 = int(assignment_pair[1].split("-")[0]), int(assignment_pair[1].split("-")[1])
        if (s1>=s2 and e1<=e2) or (s2>=s1 and e2<=e1):
            overlaps +=1

    return overlaps

def get_partial_overlaps():
    input_lines = util.read_input(day=4)
    assignments = [pair.strip("\n").split(",") for pair in input_lines]
    overlaps = 0
    for assignment_pair in assignments:
        s1, e1 = int(assignment_pair[0].split("-")[0]), int(assignment_pair[0].split("-")[1])
        s2, e2 = int(assignment_pair[1].split("-")[0]), int(assignment_pair[1].split("-")[1])
        s1,e1, s2, e2 = (s1,e1, s2, e2 ) if s2>s1 else (s2,e2,s1,e1)
        if not( s2 > e1 ):
            overlaps += 1

    return overlaps


print(get_partial_overlaps())