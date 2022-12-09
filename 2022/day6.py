import util

def get_first_packet_char():
    input = util.read_input(day=6)[0].strip("\n").strip()
    p = None
    for p in range(14, len(input)):
        s = set([c for c in input[p-14:p]])
        if len(s) == 14:
            break

    return p



print(get_first_packet_char())