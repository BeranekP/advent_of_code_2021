
def import_data(filename:str):
    with open(filename) as f:
        data = list(map(int,f.read().split(',')))
    return data

data = import_data('input.txt')
days = [80, 256]
generations = 8

def init(data, generations):
    fish={}
    for gen in range(generations + 1):
        fish[gen]=0

    for v in data:
        fish[v]+=1

    return fish

def populate(intital_state, days):
    for _ in range(days):
        old_fish = intital_state.copy()
        for gen in old_fish:
            match gen:
                case 8:
                    intital_state[gen] = old_fish[0]
                case 6:
                    intital_state[gen] = old_fish[0] + old_fish[7]
                case _:
                    intital_state[gen] = old_fish[gen + 1]

    return sum(intital_state.values())


initial = init(data, generations)
for d in days:
    print(f'{d} days: ', populate(initial, d))


    
        

