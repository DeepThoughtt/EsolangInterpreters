class TickInterpreter:

    def __init__(self, code):
        self.code = code
        self.tape = {0 : 0}
        self.tptr = 0
        
    
    def run(self):
        out = ""
        
        for command in self.code:
            if command == "+":
                self.tape[self.tptr] = (self.tape[self.tptr] + 1) % 256
            
            if command == "*":
                out += chr(self.tape[self.tptr])
                
            if command == "<":
                self.tptr -= 1
                if self.tptr not in self.tape.keys():
                    self.tape[self.tptr] = 0
                    
            if command == ">":
                self.tptr += 1
                if self.tptr not in self.tape.keys():
                    self.tape[self.tptr] = 0
                    
        return out
        
