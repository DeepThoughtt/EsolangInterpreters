class ForRealInterpreter:

    def __init__(self, code, user_input = ""):
        self.code = code
        self.user_input = list(user_input)
        self.memory = {0 : 0}
        
        self.cptr = 0
        self.mptr = 0
        self.out = ""
        
        self.closed_brackets = {}
        self.open_brackets = {}
        brackets = []
        
        i = 0
        while i < len(self.code):
            if self.code[i] == "l":
                brackets.append(i)
            elif self.code[i] == "L":
                b = brackets.pop()
                self.closed_brackets[b] = i
                self.open_brackets[i] = b
                
            i += 1
            
            
    def run(self):
        commands = {
            "4" : self.__increment_data,
            "r" : self.__decrement_data,
            "e" : self.__move_mptr_right,
            "a" : self.__move_mptr_left,
            "l" : self.__eval_open_bracket,
            "R" : self.__get_and_store,
            "E" : self.__append_to_out,
            "L" : self.__eval_closed_bracket,
        }
        
        while self.cptr < len(self.code) and self.code[self.cptr] != "A":
            if self.code[self.cptr] in commands.keys():
                commands[self.code[self.cptr]]()
            
            self.cptr += 1
            
        return self.out
    
    
    def __increment_data(self):
        self.memory[self.mptr] = (self.memory[self.mptr] + 1) % 256
        
    
    def __decrement_data(self):
        self.memory[self.mptr] = (self.memory[self.mptr] - 1) % 256
        
    
    def __move_mptr_right(self):
        self.mptr += 1
        
        if self.mptr not in self.memory.keys():
            self.memory[self.mptr] = 0
            
    
    def __move_mptr_left(self):
        self.mptr -= 1
        
        if self.mptr not in self.memory.keys():
            self.memory[self.mptr] = 0
        
    
    def __eval_open_bracket(self):
        if self.memory[self.mptr] == 0:
            self.cptr = self.closed_brackets[self.cptr]
            
    
    def __eval_closed_bracket(self):
        if self.memory[self.mptr] != 0:
            self.cptr = self.open_brackets[self.cptr]
            
    
    def __get_and_store(self):
        self.memory[self.mptr] = ord(self.user_input.pop(0))
    
    
    def __append_to_out(self):
        self.out += chr(self.memory[self.mptr])
    
