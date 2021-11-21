class InfiniTickInterpreter:

    def __init__(self, code):
        self.memory = {0 : 0}
        self.code = code
        self.out = ""
        self.ptr = 0
        self.cptr = 0
        self.skip = False
        self.back_flag = False
        
        
    def run(self):
        commands = {
            ">" : self.__move_forward,
            "<" : self.__move_backwards,
            "+" : self.__increment_data_cell,
            "-" : self.__decrement_data_cell,
            "*" : self.__add_to_out_string,
            "/" : self.__skip_if_zero,
            "\\": self.__skip_if_not_zero
        }
        
        while self.code[self.cptr] != "&":
            if self.skip:
                self.skip = False
            
            else:
                if self.code[self.cptr] in commands.keys():
                    commands[self.code[self.cptr]]()
            
            if self.back_flag:
                self.back_flag = False
            
            else:
                self.cptr += 1
        
        return self.out
        
    
    def __move_forward(self):
        self.ptr += 1
        
        if self.ptr not in self.memory.keys():
            self.memory[self.ptr] = 0
        
    
    def __move_backwards(self):
        self.ptr -= 1
        
        if self.ptr not in self.memory.keys():
            self.memory[self.ptr] = 0
        
    
    def __increment_data_cell(self):
        self.memory[self.ptr] = (self.memory[self.ptr] + 1) % 256
        
    
    def __decrement_data_cell(self):
        self.memory[self.ptr] = (self.memory[self.ptr] - 1) % 256
    
    
    def __add_to_out_string(self):
        self.out += chr(self.memory[self.ptr])
        
    
    def __skip_if_zero(self):
        if self.memory[self.ptr] == 0:
            if self.code[self.cptr + 1] != "&":
                self.skip = True
            
            else:
                self.cptr = 0
                self.back_flag = True
        
    
    def __skip_if_not_zero(self):
        if self.memory[self.ptr] != 0:
            if self.code[self.cptr + 1] != "&":
                self.skip = True
            
            else:
                self.cptr = 0
                self.back_flag = True
                
