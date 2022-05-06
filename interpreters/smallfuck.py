class SmallfuckInterpreter:

    def __init__(self, code, tape):
        self.codelist = [x for x in code.replace("[]", "")]
        self.tapelist = [x for x in tape]
        self.code_ptr = 0
        self.tape_ptr = 0
        
        self.closed_brackets = {}
        self.open_brackets = {}
        brackets = []
        
        i = 0
        while i < len(self.codelist):
            if self.codelist[i] == "[":
                brackets.append(i)
            elif self.codelist[i] == "]":
                b = brackets.pop()
                self.closed_brackets[b] = i
                self.open_brackets[i] = b
                
            i += 1
        
    
    def run(self):
        operations = {
            "*" : self.__switch_bit,
            ">" : self.__step_forward,
            "<" : self.__step_backwards,
            "[" : self.__eval_open_bracket,
            "]" : self.__eval_closed_bracket
        }
        
        while self.code_ptr < len(self.codelist) and self.tape_ptr >= 0 and self.tape_ptr < len(self.tapelist):
            if self.codelist[self.code_ptr] in operations.keys():
                operations[self.codelist[self.code_ptr]]()
            
            self.code_ptr += 1
            
        return "".join(self.tapelist)
        
        
    def __switch_bit(self):
        if self.tapelist[self.tape_ptr] == "0":
            self.tapelist[self.tape_ptr] = "1"
        else:
            self.tapelist[self.tape_ptr] = "0"
        
        
    def __step_forward(self):
        self.tape_ptr += 1
        
        
    def __step_backwards(self):
        self.tape_ptr -= 1
        
    
    def __eval_open_bracket(self):
        if self.tapelist[self.tape_ptr] == "0":
            self.code_ptr = self.closed_brackets[self.code_ptr]
            
    
    def __eval_closed_bracket(self):
        if self.tapelist[self.tape_ptr] == "1":
            self.code_ptr = self.open_brackets[self.code_ptr]
            
