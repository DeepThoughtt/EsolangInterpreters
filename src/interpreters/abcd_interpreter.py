from src.base.esolang_interpreter import EsolangInterpreter

class AbcdInterpreter(EsolangInterpreter):

    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".ab"],
            increment_cell_value_instruction = "A",
            decrement_cell_value_instruction = "B",
            input_instruction = "C",
            print_instruction = "D",
        )
