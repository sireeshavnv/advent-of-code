import util

def get_tail_positions():
    moves = util.read_input(day=9)
    tail_positions = [(0,0)]

    def make_move(head_pos, tail_pos, dir):
        if abs(head_pos[0] - tail_pos[0]) >1:
            tail_pos[0] = tail_pos[0] + 1  if(head_pos[0] - tail_pos[0]) > 0 else tail_pos[0] - 1
            if head_pos[1] - tail_pos[1] !=0:
                 # make the move diagonal
                tail_pos[1] = tail_pos[1] + 1 if head_pos[1] > tail_pos[1] else tail_pos[1] - 1
        elif abs(head_pos[1] - tail_pos[1]) >1:
            tail_pos[1] = tail_pos[1] + 1 if (head_pos[1] - tail_pos[1]) > 0 else tail_pos[1]-1
            if head_pos[0] - tail_pos[0] !=0:
                # make the move diagonal
                tail_pos[0] = tail_pos[0] + 1 if head_pos[0] > tail_pos[0] else tail_pos[0] - 1

        return tail_pos

    move_coor = {'R': (1, 0), 'L': (-1, 0), 'U': [0, 1], 'D': [0, -1]}
    no_knots = 10 # set this to 2 for part 1 of the problem
    knots_position=[[0,0] for _ in range(no_knots)]
    for move in moves:
        dir, no_moves = move.strip().split(" ")[0], int(move.strip().split(" ")[1])
        for step in range(no_moves):
            knots_position[0][0] +=move_coor[dir][0]
            knots_position[0][1] +=move_coor[dir][1]
            knot = 1
            while knot < len(knots_position):
                tail = make_move(knots_position[knot-1],knots_position[knot],dir)
                knots_position[knot] = tail
                knot = knot+ 1
            tail_positions.append(tuple(knots_position[-1]))


    return len(set(tail_positions))


print(get_tail_positions())






