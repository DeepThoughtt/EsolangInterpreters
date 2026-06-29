from src.base.esolang_interpreter import EsolangInterpreter

class PaintfuckInterpreter(EsolangInterpreter):

    def __init__(self, filename, iterations, width, height):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = ".pf",
        )

        self.width = width
        self.height = height

        # In Paintfuck memory is a grid
        row = [0] * width
        self.memory = [row.copy() for _ in range(height)]

        # Every code instruction executed equals to an iteration done
        self.iterations = iterations

        # Pointer coordinates in the grid
        self.x_pointer = 0
        self.y_pointer = 0

        self.add_instruction("[", self.eval_open_loop)
        self.add_instruction("]", self.eval_closed_loop)
        self.setup_loop_dicts("[", "]")

        self.add_instruction("n", self.move_north)
        self.add_instruction("s", self.move_south)
        self.add_instruction("w", self.move_west)
        self.add_instruction("e", self.move_east)

    def run(self):
        iteration_counter = 0

        while self.source_code_pointer < len(self.source_code_pointer) and iteration_counter < self.iterations:
            if self.source_code[self.source_code_pointer] in self.language_instructions.keys():
                self.language_instructions[self.source_code[self.source_code_pointer]]()
                iteration_counter += 1
                
            self.source_code_pointer += 1

        result = []
        for line in self.memory:
            result.append(str(bit) for bit in line)
            
        return "\r\n".join(result)

    def eval_open_loop(self):
        if self.memory[self.y_pointer][self.x_pointer] == 0:
            self.source_code_pointer = self.closed_loop_instructions[self.source_code_pointer]

    def eval_closed_loop(self):
        if self.memory[self.y_pointer][self.x_pointer] == 1:
            self.source_code_pointer = self.open_loop_instructions[self.source_code_pointer]

    def move_north(self):
        self.y_pointer = (self.y_pointer - 1) % self.height
        
    def move_south(self):
        self.y_pointer = (self.y_pointer + 1) % self.height
        
    def move_east(self):
        self.x_pointer = (self.x_pointer + 1) % self.width
        
    def move_west(self):
        self.x_pointer = (self.x_pointer - 1) % self.width

    def flip_bit(self):
        if self.memory[self.y_pointer][self.x_pointer] == 1:
            self.memory[self.y_pointer][self.x_pointer] = 0
        else:
            self.memory[self.y_pointer][self.x_pointer] = 1
