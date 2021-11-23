class PaintfuckInterpreter:

    def __init__(self, code, iterations, width, height):
        self.code = code
        self.its = iterations
        self.width = width
        self.height = height
        self.code_ptr = 0
        self.grid = []
        
        self.x = 0
        self.y = 0
        
        i = 0
        row = [0] * width
        while i < height:
            self.grid.append(row.copy())
            i += 1
            
        self.closed_brackets = {}
        self.open_brackets = {}
        brackets = []
        
        i = 0
        while i < len(self.code):
            if self.code[i] == "[":
                brackets.append(i)
            elif self.code[i] == "]":
                b = brackets.pop()
                self.closed_brackets[b] = i
                self.open_brackets[i] = b
                
            i += 1
        
        
    def run(self):
        commands = {
            "n" : self.__move_north,
            "s" : self.__move_south,
            "e" : self.__move_east,
            "w" : self.__move_west,
            "*" : self.__flip_bit,
            "[" : self.__eval_open_bracket,
            "]" : self.__eval_closed_bracket
        }
        
        counter = 0
        while self.code_ptr < len(self.code) and counter < self.its:
            if self.code[self.code_ptr] in commands.keys():
                commands[self.code[self.code_ptr]]()
                counter += 1
                
            self.code_ptr += 1
        
        result = []
        for line in self.grid:
            str_line = ""
            for x in line:
                str_line += str(x)
            result.append(str_line)
            
        return "\r\n".join(result)
        
    
    def __flip_bit(self):
        if self.grid[self.y][self.x] == 1:
            self.grid[self.y][self.x] = 0
        else:
            self.grid[self.y][self.x] = 1
            
    
    def __eval_open_bracket(self):
        if self.grid[self.y][self.x] == 0:
            self.code_ptr = self.closed_brackets[self.code_ptr]
            
    
    def __eval_closed_bracket(self):
        if self.grid[self.y][self.x] == 1:
            self.code_ptr = self.open_brackets[self.code_ptr]
            
            
    def __move_north(self):
        self.y = (self.y - 1) % self.height
        
        
    def __move_south(self):
        self.y = (self.y + 1) % self.height
        
        
    def __move_east(self):
        self.x = (self.x + 1) % self.width
        
        
    def __move_west(self):
        self.x = (self.x - 1) % self.width
        
