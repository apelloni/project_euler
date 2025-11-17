# Maximum Path Sum I

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


paths_lvl = [[] for _ in range(len(triangle))]

paths_lvl[0] += [[triangle[0][0]]]

# Explore each level and get the best path to reach each of the new points
for lvl, values in enumerate(triangle):
    if lvl == 0:
        continue

    for idx, v in enumerate(values):
        # check from above left
        sum_left = 0
        sum_right = 0
        if idx > 0:
            sum_left = sum(paths_lvl[lvl-1][idx-1])
        # check from above right
        if idx < len(values)-1:
            sum_right = sum(paths_lvl[lvl-1][idx])

        if sum_left > sum_right:
            paths_lvl[lvl] += [paths_lvl[lvl-1][idx-1] + [v]]
        else:
            paths_lvl[lvl] += [paths_lvl[lvl-1][idx] + [v]]


best_sum = 0
best_path = []

for paths in paths_lvl[-1]:
    s = sum(paths)
    if s > best_sum:
        best_sum = s
        best_path = paths

print(f'Sum = {best_sum}, Path = {best_path}')
