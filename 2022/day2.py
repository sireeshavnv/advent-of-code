import util

def game_score(c1, c2):
    game_possibilities = {"AX": 3 , "AY": 6 ,"AZ": 0 ,"BX": 0 ,"BY":3 ,"BZ": 6, "CX": 6 ,"CY": 0 ,"CZ": 3 }
    return game_possibilities[c1+c2]

def game_choice_by_output(c1,c2):
    game_choice_score = {"AX": 3, "AY": 1 ,"AZ": 2 ,"BX": 1 ,"BY":2 ,"BZ": 3, "CX": 2,"CY": 3 ,"CZ": 1 }
    return game_choice_score[c1+c2]

def get_total_score():
    input_lines = util.read_input(day=2)
    choice_score = {"X": 1, "Y":2, "Z":3}
    score = 0
    for choices in input_lines:
        c1,c2 = choices.strip().split(" ")
        score = score + game_score(c1,c2) + choice_score[c2]

    return score

def get_total_score_part2():
    input_lines = util.read_input(day=2)
    game_score= {"X": 0, "Y": 3, "Z": 6}
    score = 0
    for choices in input_lines:
        c1, c2 = choices.strip().split(" ")
        score = score + game_score[c2] + game_choice_by_output(c1,c2)

    return score

print(get_total_score_part2())

