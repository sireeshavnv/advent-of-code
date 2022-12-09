import util
import heapq

def get_most_calories():
    calories = util.read_input(day=1)
    calories.append("")
    most_calories = 0
    curr_total = 0
    for cal in calories:
        if cal.strip() == "":
            most_calories = max(curr_total, most_calories)
            curr_total = 0
        else:
            curr_total = curr_total + int(cal.strip())

    return most_calories

def get_top_three_calories():
    calories = util.read_input(day=1)
    calories.append("")
    curr_total = 0
    top_three = [0,0,0]
    heapq.heapify(top_three)
    for cal in calories:
        if cal.strip() == "":
            heapq.heappushpop(top_three,curr_total)
            curr_total = 0
        else:
            curr_total = curr_total + int(cal.strip())

    return sum(top_three)

print(get_top_three_calories())


