from src.base.esolang_interpreter import EsolangInterpreter

class AbcdInterpreter(EsolangInterpreter):

    def __init__(self, source_code_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = [".ab"],
            increment_cell_value_instruction = "A",
            decrement_cell_value_instruction = "B",
            input_instruction = "C",
            print_instruction = "D",
        )
