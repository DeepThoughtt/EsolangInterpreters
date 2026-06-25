from base.interpreter import Interpreter

class BrainfuckInterpreter(Interpreter):
    
    def __init__(self, filename):

        super().__init__(
            allowed_source_file_extensions = [".bf"],
            open_loop_symbol = "[",
            closed_loop_symbol = "]",
            filename = filename
        )