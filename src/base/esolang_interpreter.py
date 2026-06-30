import pathlib

class EsolangInterpreter:

    def __init__(
        self, 
        allowed_source_file_extensions, 
        source_code_file, 
        open_loop_instruction = None,
        closed_loop_instruction = None, 
        print_instruction = None, 
        input_instruction = None,
        move_pointer_left_instruction = None, 
        move_pointer_right_instruction = None,
        increment_cell_value_instruction = None,
        decrement_cell_value_instruction = None,
        flip_bit_instruction = None,
    ):
        
        self.allowed_source_file_extensions = tuple(allowed_source_file_extensions)
        source_code_file_path = pathlib.Path(source_code_file)

        if not source_code_file_path.is_file():
            raise ValueError("File not found")

        if not source_code_file.endswith(self.allowed_source_file_extensions):
            raise ValueError("Invalid file extension")
        
        with open(source_code_file, "r", encoding = "utf-8") as source_code_file_content:
            self.source_code = source_code_file_content.read()

        # The key is the memory cell index, the value is the value inside the cell
        self.memory = {0 : 0}
        self.memory_pointer = 0
        self.source_code_pointer = 0

        self.closed_loop_instructions = {}
        self.open_loop_instructions = {}
        self.language_instructions = {}

        if open_loop_instruction != None and closed_loop_instruction != None:
            self.language_instructions[open_loop_instruction] = self.eval_open_loop
            self.language_instructions[closed_loop_instruction] = self.eval_closed_loop
            self.setup_loop_dicts(open_loop_instruction, closed_loop_instruction)
        
        if input_instruction != None:
            self.add_instruction(input_instruction, self.input_character)
        
        if print_instruction != None:
            self.add_instruction(print_instruction, self.print_character)

        if move_pointer_left_instruction != None:
            self.add_instruction(move_pointer_left_instruction, self.move_pointer_left)

        if move_pointer_right_instruction != None:
            self.add_instruction(move_pointer_right_instruction, self.move_pointer_right)

        if increment_cell_value_instruction != None:
            self.add_instruction(increment_cell_value_instruction, self.increment_cell_value)

        if decrement_cell_value_instruction != None:
            self.add_instruction(decrement_cell_value_instruction, self.decrement_cell_value)

        if flip_bit_instruction != None:
            self.add_instruction(flip_bit_instruction, self.flip_bit)

    def run(self):
        while self.source_code_pointer < len(self.source_code):
            if self.source_code[self.source_code_pointer] in self.language_instructions.keys():
                instruction = self.source_code[self.source_code_pointer]
                self.language_instructions[instruction]()

            self.source_code_pointer += 1

    def add_instruction(self, instruction, called_function):
        self.language_instructions[instruction] = called_function

    def setup_loop_dicts(self, open_loop_instruction, closed_loop_instruction):
        loop_instructions = []
        i = 0

        while i < len(self.source_code):
            if self.source_code[i] == open_loop_instruction:
                loop_instructions.append(i)

            elif self.source_code[i] == closed_loop_instruction:
                instruction = loop_instructions.pop()
                self.closed_loop_instructions[instruction] = i
                self.open_loop_instructions[i] = instruction
                
            i += 1

    def eval_open_loop(self):
        if self.memory[self.memory_pointer] == 0:
            self.source_code_pointer = self.closed_loop_instructions[self.source_code_pointer]

    def eval_closed_loop(self):
        if self.memory[self.memory_pointer] != 0:
            self.source_code_pointer = self.open_loop_instructions[self.source_code_pointer]

    def print_character(self):
        character = chr(self.memory[self.memory_pointer])
        print(character, end = "")

    def input_character(self):
        inserted_character = input()
        
        # The user wrote nothing
        if inserted_character == None:
            return

        character_code = ord(inserted_character)
        self.memory[self.memory_pointer] = character_code

    def move_pointer_left(self):
        self.memory_pointer -= 1
        
        if self.memory_pointer not in self.memory.keys():
            self.memory[self.memory_pointer] = 0

    def move_pointer_right(self):
        self.memory_pointer += 1
        
        if self.memory_pointer not in self.memory.keys():
            self.memory[self.memory_pointer] = 0

    def increment_cell_value(self):
        self.memory[self.memory_pointer] = (self.memory[self.memory_pointer] + 1) % 256

    def decrement_cell_value(self):
        self.memory[self.memory_pointer] = (self.memory[self.memory_pointer] - 1) % 256

    def flip_bit(self):
        if self.memory[self.memory_pointer] == 0:
            self.memory[self.memory_pointer] = 1
        else:
            self.memory[self.memory_pointer] = 0
