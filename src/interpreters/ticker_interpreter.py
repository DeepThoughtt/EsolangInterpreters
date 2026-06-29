from src.base.esolang_interpreter import EsolangInterpreter

class TickerInterpreter(EsolangInterpreter):

    def __init__(self, source_code_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = [".ticker"],
            increment_cell_value_instruction = "+",
            decrement_cell_value_instruction = "-",
        )

        self.next_cell = 0
        self.add_instruction(">", self.move_pointer_right)
        self.add_instruction("<", self.move_pointer_left)
        self.add_instruction("/", self.set_data_to_zero)
        self.add_instruction("*", self.print_character)
        self.add_instruction("!", self.add_cell)
        

    def move_pointer_left(self):
        self.memory_pointer -= 1

    def move_pointer_right(self):
        self.memory_pointer += 1

    def print_character(self):
        if self.memory_pointer in self.memory:
            print(chr(self.memory[self.memory_pointer]))
        else:
            print(chr(0))

    def set_data_to_zero(self):
        if self.memory_pointer in self.memory:
            self.memory[self.memory_pointer] = 0

    def add_cell(self):
        self.memory[self.next_cell] = 0
        self.next_cell += 1