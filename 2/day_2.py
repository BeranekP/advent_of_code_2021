## import data
def aoc_import_file(filename:str) -> list[str]:
    with open(filename) as f:
        output_data =f.read().strip().split('\n')
    
    return output_data

## Submarine class
class Submarine:
    def __init__(self):
        self.x:int = 0 # horizontal position
        self.y:int = 0 # depth
        self.aim:int = 0 # aim
        self.commands:list[tuple[str, int]]=[] # processed commands

    def move_forward(self, amount:int):
        self.x += amount
        self.y += self.aim * amount
        
    def move_up(self, amount:int):
        #self.y -= amount # Part 1
        self.aim -= amount

    def move_down(self, amount:int):
        #self.y += amount # Part 1
        self.aim += amount

    def process_commands(self, data:list[str]):      
        for item in data:
            command, amount = item.split()
            self.commands.append((command, int(amount)))
        
    def run(self):
        for instruction in self.commands:
            command, amount = instruction
            match command:
                case 'forward':
                    self.move_forward(amount)
                case 'up':
                    self.move_up(amount)
                case 'down':
                    self.move_down(amount)

    def __repr__(self) -> str:
        return f'''Submarine:
                   Horizontal positition: {self.x}
                   Depth: {self.y}
                   -------------------------------
                   Multiple: {self.x * self.y}
                '''

## Run the submarine
if __name__ == '__main__':    
    data = aoc_import_file('input.txt')

    submarine = Submarine()
    submarine.process_commands(data)
    submarine.run()

    print(submarine)
