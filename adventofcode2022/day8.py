import util
def get_visible_trees():
    input = util.read_input(day=8)
    matrix = [ [ int(c) for c in input_line.strip("\n").strip()] for input_line in input ]
    m = len(matrix)
    n = len(matrix[0])
    visibility_matrix = [ [True if (i in (0,m-1) or j in (0,n-1)) else None for j in range(n)] for i in range(m)]

    def look_at_forest(m,n, vertical, start, end, direction):
        if vertical is True:
            for i in range(m):
                max_height = 0
                for j in range(start,end, direction):
                    if visibility_matrix[i][j] is None and matrix[i][j] > max_height:
                        visibility_matrix[i][j] = True
                    max_height = max(matrix[i][j],max_height)

        else:
            for j in range(n):
                max_height = 0
                for i in range(start,end,direction):
                    if visibility_matrix[i][j] is None and matrix[i][j] > max_height:
                        visibility_matrix[i][j] = True
                    max_height = max(matrix[i][j], max_height)



    look_at_forest(m,n,vertical=True,start=0,end=n,direction=1)
    look_at_forest(m,n,vertical=True,start=n-1,end=-1,direction=-1)
    look_at_forest(m,n,vertical=False,start=0,end=m,direction=1)
    look_at_forest(m,n,vertical=False,start=m-1,end=-1,direction=-1)

    count =  sum(1 if visibility_matrix[i][j] is True else 0 for i in range(m) for j in range(n))
    return count



def get_scenic_score():
    input = util.read_input(day=8)
    matrix = [[int(c) for c in input_line.strip("\n").strip()] for input_line in input]
    m = len(matrix)
    n = len(matrix[0])

    def look_from_tree(i,j, vertical, start, end, direction):
        tree_height = matrix[i][j]
        count = 0
        if vertical is True:
            for x in range(start,end, direction):
                if matrix[x][j] >= tree_height:
                    count = count + 1
                    break
                count = count + 1
        else:
            for y in range(start,end,direction):
                if matrix[i][y] >= tree_height:
                    count = count + 1
                    break
                count = count + 1

        return count

    max_score = 0
    for i in range(m):
        for j in range(n):
            a = look_from_tree(i,j ,vertical=True,start=i-1,end=-1,direction=-1)
            b = look_from_tree(i, j, vertical=True, start=i+1, end=n, direction=1)
            c = look_from_tree(i, j, vertical=False, start=j-1, end=-1, direction=-1)
            d = look_from_tree(i, j, vertical=False, start=j+1, end=m, direction=1)
            max_score = max(a*b*c*d, max_score)

    return max_score

print(get_scenic_score())

