import math

def import_data(filename:str) -> list[list[tuple[int,int]]]:
    with open(filename) as f:
        data = f.read().strip().split('\n')
        data = [line.split(' -> ') for line in data]
        data = [[tuple(map(int, point.split(','))) for point in line] for line in data]
                 
    return data

def is_vertical(line:list[tuple[int,int]]) -> bool:
    p1, p2 = line
    x1, _ = p1
    x2, _ = p2
    return x1 == x2

def is_horizontal(line:list[tuple[int,int]]) -> bool:
    p1, p2 = line
    _, y1 = p1
    _, y2 = p2
    return y1 == y2  

def get_points(line:list[tuple[int,int]], mode:str=None) -> list[tuple[int,int]]:
    start, end = line
    x1, y1 = start
    x2, y2 = end

    if is_vertical(line):
        points = [(x1,y) for y in range(min(y1, y2), max(y1, y2)+1)]
        return points
    if is_horizontal(line):
        points = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]
        return points  

    if mode == 'all':
        A = (y2-y1)/(x2-x1)
        if abs(A) == 1:
            A = int(A)
            B = y1 - A * x1
            points = [(x, A*x+B) for x in range(min(x1, x2), max(x1, x2)+1)]
            return points

    
def overlapped(lines: list[list[tuple[int,int]]], mode:str=None) -> dict:
    covered_points=dict()
    for line in lines:
        points =  get_points(line, mode)
        if points:
            for point in points:
                if point not in covered_points:
                    covered_points[point] = 1
                else:
                    covered_points[point] += 1 
    return covered_points

lines = import_data('input.txt')

result1 = overlapped(lines)
result2 = overlapped(lines, 'all')

print(f'Part I: {sum(amount>=2 for amount in result1.values())}')
print(f'Part II: {sum(amount>=2 for amount in result2.values())}')