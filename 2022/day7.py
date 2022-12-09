import util

class Node():
    def __init__(self,name,size=None,children=None):
        self.name = name
        self.size = size
        self.children = children

def form_tree():
    commands = util.read_input(day=7)
    stack = []
    nodes = {}
    for command in commands:
        if not (command.startswith("$")):
            size, name = command.strip("\n").strip().split(" ")
            if size == "dir":
                node = Node(name=name, children=[])
            else:
                node = Node(name=name, size=int(size))
            nodes["/".join([n.name for n in stack]) + "/" + name ] = node
            stack[-1].children.append(node)
        elif command.strip() == '$ cd ..':
            stack.pop(len(stack)-1)
        elif command.strip() == '$ cd /':
            if "/" in nodes:
                node = nodes["/"]
            else:
                node = Node(name='/', children=[])
                nodes['/'] = node
            stack = [node]
        elif command.startswith("$ cd "):
            name = command.replace("$ cd ","").strip("\n").strip(" ")
            node = nodes["/".join([n.name for n in stack]) + "/" + name ]
            stack.append(node)

    return nodes

def part1():
    nodes = form_tree()
    atmost_size = 100000
    tot = 0
    for key in nodes:
        if key == "/":
            continue
        node = nodes[key]
        if node.size is None:
            size = get_node_size(node)
            if size <= atmost_size:
                print(node.name)
                tot +=size

    return tot
def get_node_size(node):
    size = 0
    for child in node.children:
        if child.size is None:
            child_size = get_node_size(child)
        else:
            child_size = child.size
        size += child_size

    return size

def part2():
    nodes = form_tree()
    total_disk = 70000000
    disk_need_for_update = 30000000
    available_space = total_disk - get_node_size(nodes["/"])
    need_space = disk_need_for_update - available_space

    curr_dir_size = None
    for key in nodes:
        if key == "/":
            continue
        node = nodes[key]
        if node.size is None:
            size = get_node_size(node)
            if size >= need_space and (curr_dir_size is None or size < curr_dir_size):
                curr_dir_size = size

    return curr_dir_size

print(part2())