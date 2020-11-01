def input_data():
    """ Read a square grid of single-digit numbers, then
        Read a target and a direction. Return all three."""

    first = [int(x) for x in input().split()]
    grid = [first]
    for i in range(len(first) - 1):
        grid.append([int(x) for x in input().split()])
    target = int(input())
    direction = int(input())
    return (grid, target, direction)
