## import data
def aoc_import_file(filename:str) -> list[int]:
    with open(filename) as f:
        output_data = map(int, f.read().strip().split())
    
    return list(output_data)

## helper function
def subtract(args:list[int]) -> int:
    return args[1] - args[0]

data = aoc_import_file('input.txt')

## First star
increasing_1 =  [subtract(d) > 0 for d in zip(data, data[1:])]
print('First part:', sum(increasing_1))


## Second star
triplets = [sum(d) for d in zip(data, data[1:], data[2:])]
increasing_2 =  [subtract(t) > 0 for t in zip(triplets, triplets[1:])]
print('Second part:', sum(increasing_2))
