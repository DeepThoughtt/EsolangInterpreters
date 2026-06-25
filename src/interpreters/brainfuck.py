from base.interpreter import Interpreter

class BrainfuckInterpreter(Interpreter):
    
    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".bf"],
            open_loop_instruction = "[",
            closed_loop_instruction = "]",
            print_instruction = ".",
            input_instruction = ",",
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
            increment_cell_value_instruction = "+",
            decrement_cell_value_instruction = "+",
        )