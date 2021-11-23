class BoolfuckInterpreter:

    def __init__(self, code, user_input = ""):
        self.user_input = user_input
        self.code = code
        self.cptr = 0
        
        self.memory = {0 : "0"}
        self.mptr = 0
        
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
        
        self.out_bits = [""]
        self.out_ptr = 0
        
        self.in_bits = []
        for char in user_input:
            self.in_bits.append(list(bin(ord(char))[2:].zfill(8)[::-1]))
    
    
    def run(self):
        commands = {
            "+" : self.__flip_bit,
            "," : self.__read_from_input,
            ";" : self.__print_to_out,
            "<" : self.__move_mptr_left,
            ">" : self.__move_mptr_right,
            "[" : self.__eval_open_bracket,
            "]" : self.__eval_closed_bracket
        }
        
        while self.cptr < len(self.code):
            if self.code[self.cptr] in commands.keys():
                commands[self.code[self.cptr]]()
            
            self.cptr += 1
            
        result = ""
        
        if self.out_bits[self.out_ptr] == "":
            del self.out_bits[len(self.out_bits) - 1]
            self.out_ptr -= 1
            
        if self.user_input != "" and len(self.out_bits[self.out_ptr]) < 8:
            self.out_bits[self.out_ptr] = self.out_bits[self.out_ptr].zfill(8)
        
        for byte in self.out_bits:
            result += chr(int(byte, 2))
        
        return result
    
    
    def __flip_bit(self):
        if self.memory[self.mptr] == "0":
            self.memory[self.mptr] = "1"
        else:
            self.memory[self.mptr] = "0"
    
    
    def __move_mptr_left(self):
        self.mptr -= 1
        if self.mptr not in self.memory.keys():
            self.memory[self.mptr] = "0"
    
    
    def __move_mptr_right(self):
        self.mptr += 1
        if self.mptr not in self.memory.keys():
            self.memory[self.mptr] = "0"
    
    
    def __eval_open_bracket(self):
        if self.memory[self.mptr] == "0":
            self.cptr = self.closed_brackets[self.cptr]
    
    
    def __eval_closed_bracket(self):
        if self.memory[self.mptr] == "1":
            self.cptr = self.open_brackets[self.cptr]
    
    
    def __read_from_input(self):
        if len(self.in_bits) == 0:
            self.memory[self.mptr] = "0"
        else:
            self.memory[self.mptr] = self.in_bits[0].pop(0)
            
            if len(self.in_bits[0]) == 0:
                del self.in_bits[0]
    
    
    def __print_to_out(self):
        self.out_bits[self.out_ptr] = str(self.memory[self.mptr]) + self.out_bits[self.out_ptr]
        
        if len(self.out_bits[self.out_ptr]) == 8:
            self.out_ptr += 1
            self.out_bits.append("")
    
