

def import_data(filename:str):
    with open(filename) as f:
        data = f.read().strip().replace('  ', ' ').split('\n\n')
    numbers, boards = data[0], data[1:]
    numbers = list(map(int, numbers.split(',')))
    boards = [[list(map(int, b.strip().split(' '))) for b in board.strip().split('\n')] for board in boards]
    return numbers, boards


def is_winning(mark:list) -> tuple[bool, list[int]]:
    for row in mark:
        if all(r != '' for r in row):
            return True, row
        
        # check columns
    for column in list(zip(*mark)):
        if all(c != '' for c in column):
            return True, column
    
    return False, None

def get_result(boards, marks, winning_board, combination, number):
    unmarked_sum = 0
    for i, row in enumerate(marks[winning_board]):
        for j, item in enumerate(row):
            if not item:
                unmarked_sum += boards[winning_board][i][j]


    print(f'Winning: {combination} | {number}\nResult: {unmarked_sum * number}')


def bingo(numbers, boards, marks, len_boards=0):
    for number in numbers:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, item in enumerate(row):
                    if item == number:
                        marks[i][j][k] = number
        
                        win, combination = is_winning(marks[i])
                        if win: 
                            if len(boards) > 1:
                                if len_boards == len(boards):
                                    print(f'*FIRST*: {board} - removing from list')
                                    get_result(boards, marks, i, combination, number)
                                
                                boards.remove(board)
                                marks.remove(marks[i])
                                
                                numbers = numbers[numbers.index(number):]
                                return bingo(numbers, boards, marks)
                            

                            else:
                                print(f'*LAST*: {marks[i]} - last board to win ')
                                get_result(boards, marks, i, combination, number)
                                return None
                                


numbers, boards = import_data('input.txt')
marks = [[['' for _ in row] for row in board] for board in boards]

bingo(numbers, boards, marks, len(boards))

