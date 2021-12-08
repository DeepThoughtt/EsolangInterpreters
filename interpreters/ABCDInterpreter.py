class ABCDInterpreter:

    def __init__(self, code, user_input = ""):
        self.code = code
        self.user_input = list(user_input)
        self.cell = 0
        
        
    def run(self):
        out = ""
        
        for cmd in self.code:
            if cmd == "A":
                self.cell += 1
            elif cmd == "B":
                self.cell -= 1
            elif cmd == "C":
                self.cell = ord(self.user_input.pop(0))
            elif cmd == "D":
                out += chr(self.cell)
        
        return out
        
