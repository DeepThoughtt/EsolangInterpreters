class TickerInterpreter:

    def __init__(self, code):
        self.memory = {0 : 0}
        self.code = code
        self.mptr = 0
        self.next_cell = 1
        self.out = ""
        
    
    def run(self):
        commands = {
            ">" : self.__increment_selector,
            "<" : self.__decrement_selector,
            "+" : self.__increment_data,
            "-" : self.__decrement_data,
            "/" : self.__set_data_to_zero,
            "!" : self.__add_cell,
            "*" : self.__add_ascii
        }
        
        for instruction in self.code:
            if instruction in commands.keys():
                commands[instruction]()
        
        return self.out
        
        
    def __increment_selector(self):
        self.mptr += 1
    
    
    def __decrement_selector(self):
        self.mptr -= 1
        
    
    def __increment_data(self):
        if self.mptr in self.memory.keys():
            self.memory[self.mptr] = (self.memory[self.mptr] + 1) % 256
            
    
    def __decrement_data(self):
        if self.mptr in self.memory.keys():
            self.memory[self.mptr] = (self.memory[self.mptr] - 1) % 256
            
    
    def __set_data_to_zero(self):
        if self.mptr in self.memory.keys():
            self.memory[self.mptr] = 0
            
            
    def __add_cell(self):
        self.memory[self.next_cell] = 0
        self.next_cell += 1
            
    
    def __add_ascii(self):
        if self.mptr in self.memory.keys():
            self.out += chr(self.memory[self.mptr])
        else:
            self.out += chr(0)
            
