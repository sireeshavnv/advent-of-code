import util


def get_top_elements():
    input_lines = util.read_input(day=5)
    stacks, iter = get_stacks(input_lines)
    print(stacks)
    for instruction_line in range(iter + 1, len(input_lines)):
        instruction = input_lines[instruction_line].split(" ")
        count, from_stack, to_stack = int(instruction[1]), int(instruction[3]), int(instruction[5])

        while count:
            element = stacks[from_stack - 1].pop(0)
            stacks[to_stack - 1].insert(0, element)
            count = count - 1

    result = ""
    for stack in stacks:
        result += stack[0]

    return result


def get_top_elements_part2():
    input_lines = util.read_input(day=5)
    stacks, iter = get_stacks(input_lines)

    for instruction_line in range(iter + 1, len(input_lines)):
        instruction = input_lines[instruction_line].split(" ")
        count, from_stack, to_stack = int(instruction[1]), int(instruction[3]), int(instruction[5])

        elements = []
        while count:
            elements.append(stacks[from_stack - 1].pop(0))
            count = count - 1

        while elements:
            element = elements.pop(len(elements) - 1)
            stacks[to_stack - 1].insert(0, element)

    result = ""
    for stack in stacks:
        result += stack[0]
    return result


def get_stacks(input_lines):
    l = 0
    # get max length of the input with stack information. use the length to calculate number of stacks
    for input in input_lines:
        if input.strip().strip("\n") == "":
            break
        l = max(l, len(input))

    no_stacks = (l + 1) // 4
    stacks = [[] for _ in range(no_stacks)]
    for iter, input in enumerate(input_lines):
        i = 0
        if input.strip().strip("\n") == "":
            break
        for p in range(0, len(input.strip("\n")), 4):
            stacks[i].append(input[p:p + 4].strip().strip('[').strip(']'))
            i = i + 1
            # print(stacks)

    for stack in stacks:
        stack.pop(len(stack) - 1)
        while stack[0] == "":
            stack.pop(0)

    return stacks, iter


print(get_top_elements_part2())
