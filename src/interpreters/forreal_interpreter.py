from src.base.esolang_interpreter import EsolangInterpreter

class ForrealInterpreter(EsolangInterpreter):

    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".fr"],
            increment_cell_value_instruction = "4",
            decrement_cell_value_instruction = "r",
            move_pointer_right_instruction = "e",
            move_pointer_left_instruction = "a",
            open_loop_instruction = "l",
            print_instruction = "R",
            input_instruction = "E",
            closed_loop_instruction = "L",
        )
