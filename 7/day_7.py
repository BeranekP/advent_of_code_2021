from statistics import median, mean
from math import floor, ceil

def import_data(filename):
    with open(filename) as f:
        data = tuple(map(int, f.read().strip().split(',')))
    return data


data = import_data('input.txt')


def find_fuels(data):
    med = int(median(data))

    round_up =  ceil(mean(data))
    round_down =  floor(mean(data))

    fuel1 = 0
    fuel2_up = 0
    fuel2_down = 0
    
    for v in data:
        
        fuel2_up +=  ((v-round_up)**2 + abs(v - round_up)) / 2
        fuel2_down +=  ((v-round_down)**2 + abs(v - round_down)) / 2
        fuel1 += abs(v - med)

    return fuel1, int(min(fuel2_up, fuel2_down))

fuels1, fuels2 = find_fuels(data)

print('Part 1: ', fuels1)
print('Part 2: ', fuels2)

