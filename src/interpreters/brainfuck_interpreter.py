from src.base.esolang_interpreter import EsolangInterpreter

class BrainfuckInterpreter(EsolangInterpreter):
    
    def __init__(self, source_code_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = [".bf"],
            open_loop_instruction = "[",
            closed_loop_instruction = "]",
            print_instruction = ".",
            input_instruction = ",",
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
            increment_cell_value_instruction = "+",
            decrement_cell_value_instruction = "-",
        )
