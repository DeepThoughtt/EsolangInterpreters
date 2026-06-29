from src.base.esolang_interpreter import EsolangInterpreter

class MiniStringFuckInterpreter(EsolangInterpreter):

    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".msf"],
            increment_cell_value_instruction = "+",
            print_instruction = ".",
        )
