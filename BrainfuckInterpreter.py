class BrainfuckInterpreter:

    def __init__(self, code, p_input):
        self.p_input = p_input
        self.p_index = 0
        
        self.memory = {0 : 0}
        self.code = code
        self.out = ""
        self.cptr = 0
        self.dptr = 0
        
        self.closed_brackets = {}
        self.open_brackets = {}
        brackets = []
        
        i = 0
        while i < len(self.code):
            if self.code[i] == "[":
                brackets.append(i)
            elif self.code[i] == "]":
                b = brackets.pop(len(brackets) - 1)
                self.closed_brackets[b] = i
                self.open_brackets[i] = b
                
            i += 1
            
    
    def run(self):
        commands = {
            ">" : self.__move_dptr_right,
            "<" : self.__move_dptr_left,
            "+" : self.__increment_data,
            "-" : self.__decrement_data,
            "." : self.__append_to_out,
            "," : self.__get_input_byte,
            "[" : self.__eval_open_bracket,
            "]" : self.__eval_closed_bracket
        }
        
        while self.cptr < len(self.code):
            if self.code[self.cptr] in commands.keys():
                commands[self.code[self.cptr]]()
            
            self.cptr += 1
            
        return self.out
        
    
    def __move_dptr_right(self):
        self.dptr += 1
        
        if self.dptr not in self.memory.keys():
            self.memory[self.dptr] = 0
            
    
    def __move_dptr_left(self):
        self.dptr -= 1
        
        if self.dptr not in self.memory.keys():
            self.memory[self.dptr] = 0
    
    
    def __increment_data(self):
        self.memory[self.dptr] = (self.memory[self.dptr] + 1) % 256
        
    
    def __decrement_data(self):
        self.memory[self.dptr] = (self.memory[self.dptr] - 1) % 256
        
    
    def __append_to_out(self):
        self.out += chr(self.memory[self.dptr])
        
        
    def __get_input_byte(self):
        self.memory[self.dptr] = ord(self.p_input[self.p_index])
        self.p_index += 1
        
    
    def __eval_open_bracket(self):
        if self.memory[self.dptr] == 0:
            self.cptr = self.closed_brackets[self.cptr]
            
    
    def __eval_closed_bracket(self):
        if self.memory[self.dptr] != 0:
            self.cptr = self.open_brackets[self.cptr]
            
