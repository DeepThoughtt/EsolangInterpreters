from src.base.esolang_interpreter import EsolangInterpreter

class TickInterpreter(EsolangInterpreter):

    def __init__(self, source_code_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = ["tick"],
            increment_cell_value_instruction = "+",
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
            print_instruction = "*",
        )
