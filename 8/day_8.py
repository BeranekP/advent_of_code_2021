def import_data(filename):
    with open(filename) as f:
        data = f.read().split('\n')
        data = [line.split(' | ') for line in data]

    return data

data=import_data('input.txt')

## Part 1 #######################
unique = 0
for line in data:
    _, output = line
    for item in output.split():
        if len(item) in [2, 3, 4, 7]:
            unique += 1

## Part 2 ####################
total = 0

for line in data:
    digits = dict()
    numbers, output = line

    sorted_items = sorted([*numbers.split(), *output.split()], key=len)
    result = ''

    ## Resolve unique combinations
    for item in sorted_items:
        if len(item) == 2:
            digits.setdefault(1, set(item))
        if len(item) == 3:
            digits.setdefault(7, set(item))
        if len(item) == 4:
            digits.setdefault(4, set(item))
        if len(item) == 7:
            digits.setdefault(8, set(item))
    
    ## helper segment
    topangle = digits[4].difference(digits[1]) # top left angle L
    
    ## Deduce the rest
    for item in sorted_items:
        item = set(item)

        ## numbers 0, 6 , 9
        if len(item) == 6:
            ## if contains 4 --> it must be 9 
            if digits[4].issubset(item):
                digits.setdefault(9, item)
            ## if contains 7 and not 4 --> it must be 0 
            elif digits[7].issubset(item):
                digits.setdefault(0, item)
            ## otherwise it is 6    
            else: digits.setdefault(6, item)
        ## numbers 2, 3, 5    
        if len(item) == 5:
            ## if contains 1 --> it must be 3 
            if digits[1].issubset(item):
                digits.setdefault(3, item)
            ## if contains helper angle --> it must be 5 
            elif item.intersection(topangle) == topangle:
                digits.setdefault(5, item)  
            ## otherwise it is 2
            else: digits.setdefault(2, item)

    ## Decode output        
    for item in output.split():
        for k,v in digits.items():
            if set(item) == v:
                result += str(k)
    
    total += int(result)

print(total)