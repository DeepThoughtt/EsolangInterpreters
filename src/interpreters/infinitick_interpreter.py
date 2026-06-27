from src.base.esolang_interpreter import EsolangInterpreter

class InfiniTickInterpreter(EsolangInterpreter):

    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".tick"],
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
            increment_cell_value = "+",
            decrement_cell_value = "-",
            print_instruction = "*",
        )
        
        self.add_instruction("\\", self.skip_if_not_zero)
        self.add_instruction("/", self.skip_if_zero)
        self.skip_next_instruction = False
        self.back_flag = False

    def run(self):
        while self.source_code[self.source_code_pointer] != "&":
            if self.skip_next_instruction:
                self.skip_next_instruction = False
                
            else:
                if self.source_code[self.source_code_pointer] in self.language_instructions.keys():
                    instruction = self.source_code[self.source_code_pointer]
                    self.language_instructions[instruction]()
            
            if self.back_flag:
                self.back_flag = False
            else:
                self.source_code_pointer += 1

    def skip_if_zero(self):
        if self.memory[self.memory_pointer] == 0:
            if self.source_code[self.source_code_pointer + 1] != "&":
                self.skip_next_instruction = True
        
            else:
                self.source_code_pointer = 0
                self.back_flag = True

    def skip_if_not_zero(self):
        if self.memory[self.memory_pointer] != 0:
            if self.source_code[self.source_code_pointer + 1] != "&":
                self.skip_next_instruction = True
            
            else:
                self.source_code_pointer = 0
                self.back_flag = True
