## import data
def aoc_import_file(filename:str) -> list[str]:
    with open(filename) as f:
        output_data = f.read().strip().split('\n')
    
    return output_data

data = [list(map(int, list(line))) for line in aoc_import_file('input.txt')]

## helper functions
def get_major(line):
        if sum(line) >= len(line) / 2: ## 1 is major
            return True
        return False

def get_minor(line):
    return not(get_major(line))


## Part 1
transposed = list(zip(*data))
gamma = []
epsilon = []

for line in transposed:
    match get_major(line):
        case True: 
            gamma.append('1')
            epsilon.append('0')
        case False: 
            gamma.append('0')
            epsilon.append('1')
        

gamma_dec = int(''.join(gamma), 2)
epsilon_dec = int(''.join(epsilon), 2)
print(f'Part I: {gamma_dec * epsilon_dec}')

## Part 2

def filter_data(data, mode):
    filtered = data[:]
    
    for i in range(len(filtered[0])):
        
        transposed = list(zip(*filtered))
        
        if mode == 'o2':
            filter_by = int(get_major(transposed[i])) 
        else:
            filter_by = int(get_minor(transposed[i])) 
        
        filtered = [line for line in filtered if line[i] == filter_by]
        
        if len(filtered) == 1: ## Stop if only 1 number left
             return filtered[0]

    return filtered[0]

o2 = ''.join(str(v) for v in filter_data(data, 'o2'))
co2 = ''.join(str(v) for v in filter_data(data, 'co2'))
print(f'PartII: {int(o2, 2) * int(co2, 2)}')


