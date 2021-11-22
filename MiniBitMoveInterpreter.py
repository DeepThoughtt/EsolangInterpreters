class MiniBitMoveInterpreter:

    def __init__(self, code, data):
        self.code = code
        self.data = list(data)
        self.cptr = 0
        self.dptr = 0
        
    
    def run(self):
        while self.dptr < len(self.data):
            if self.code[self.cptr] == "1":
                self.data[self.dptr] = "1" if self.data[self.dptr] == "0" else "0"
            
            elif self.code[self.cptr] == "0":
                self.dptr += 1
                
            self.cptr = (self.cptr + 1) % len(self.code)
        
        return "".join(self.data)
        
