import pathlib

from src.base.esolang_interpreter import EsolangInterpreter

class SmallfuckInterpreter(EsolangInterpreter):

    def __init__(self, source_code_file, data_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = ["sf"],
            open_loop_instruction = "[",
            closed_loop_instruction = "]",
            flip_bit_instruction = "*",
        )

        self.add_instruction(">", self.move_pointer_right)
        self.add_instruction("<", self.move_pointer_left)

        data_file_path = pathlib.Path(data_file)

        if not data_file_path.is_file():
            raise ValueError("File not found")

        if not data_file.endswith(".sfdata"):
            raise ValueError("Invalid data file extension")
        
        # Smallfuck requires a source code file and a data file
        with open(data_file, "r", encoding = "utf-8") as data_file:
            file_content = data_file.read()

            for i in range(len(file_content)):
                if file_content[i] == "0" or file_content == "1":
                    self.memory[i] = int(file_content[i])

    def run(self):
        # We keep executing code until we end out of bounds, either on the source code or the memory
        while self.source_code_pointer < len(self.source_code) and self.memory_pointer >= 0 and self.memory_pointer < len(self.memory):
            if self.source_code[self.source_code_pointer] in self.language_instructions.keys():
                instruction = self.source_code[self.source_code_pointer]
                self.language_instructions[instruction]()

            self.source_code_pointer += 1
        
        return "".join(str(bit) for bit in self.memory.values())

    def move_pointer_left(self):
        self.memory_pointer -= 1

    def move_pointer_right(self):
        self.memory_pointer += 1
