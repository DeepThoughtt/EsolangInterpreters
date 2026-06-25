class Interpreter:

    def __init__(self, allowed_source_file_extensions, filename, open_loop_instruction = None, closed_loop_instruction = None, print_instruction = None, input_instruction = None):
        self.allowed_source_file_extensions = tuple(allowed_source_file_extensions)

        if self.invalid_file_extension(filename):
            raise ValueError("Invalid file extension")

        self.open_loop_instruction = open_loop_instruction
        self.closed_loop_instruction = closed_loop_instruction
        self.print_instruction = print_instruction
        self.input_instruction = input_instruction
        
        with open(filename, "r", encoding = "utf-8") as source_code_file:
            self.source_code = source_code_file.read()

        # The key is the memory cell index, the value is the value inside the cell
        self.memory = {0 : 0}
        self.memory_pointer = 0
        self.source_code_pointer = 0

        self.closed_loop_instructions = {}
        self.open_loop_instructions = {}
        self.language_instructions = {}

        if self.loop_instructions_defined():
            self.setup_loop_instructions_dicts()
            self.setup_loop_instructions()
        
        if self.input_instruction_defined():
            self.setup_input_character_instruction()
        
        if self.print_instruction_defined():
            self.setup_print_character_instruction()

    def run(self):
        while self.source_code_pointer < len(self.source_code):
            if self.source_code[self.source_code_pointer] in self.language_instructions.keys():
                instruction = self.source_code[self.source_code_pointer]
                self.language_instructions[instruction]()

            self.source_code_pointer += 1

    def invalid_file_extension(self, filename):
        return not filename.endswith(self.allowed_source_file_extensions)

    def loop_instructions_defined(self):
        return self.open_loop_instruction != None and self.closed_loop_instruction != None
    
    def input_instruction_defined(self):
        return self.input_instruction != None
    
    def print_instruction_defined(self):
        return self.print_instruction != None

    def setup_loop_instructions_dicts(self):
        loop_instructions = []
        i = 0

        while i < len(self.source_code):
            if self.source_code[i] == self.open_loop_instruction:
                loop_instructions.append(i)

            elif self.source_code[i] == self.closed_loop_instruction:
                instruction = loop_instructions.pop()
                self.closed_loop_instructions[instruction] = i
                self.open_loop_instructions[i] = instruction
                
            i += 1

    def setup_loop_instructions(self):
        self.language_instructions[self.open_loop_instruction] = self.eval_open_loop_instruction
        self.language_instructions[self.closed_loop_instruction] = self.eval_closed_loop_instruction

    def setup_print_character_instruction(self):
        self.language_instructions[self.print_instruction] = self.print_character

    def setup_input_character_instruction(self):
        self.language_instructions[self.input_instruction] = self.input_character

    def eval_open_loop_instruction(self):
        if self.memory[self.memory_pointer] == 0:
            self.source_code_pointer = self.closed_loop_instructions[self.source_code_pointer]

    def eval_closed_loop_instruction(self):
        if self.memory[self.memory_pointer] != 0:
            self.source_code_pointer = self.open_loop_instructions[self.source_code_pointer]

    def print_character(self):
        character = chr(self.memory[self.memory_pointer])
        print(character)

    def input_character(self):
        inserted_character = input()
        character_code = ord(inserted_character)
        self.memory[self.memory_pointer] = character_code
