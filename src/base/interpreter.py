class Interpreter:

    def __init__(self, allowed_source_file_extensions, filename, open_loop_symbol = None, closed_loop_symbol = None):
        self.allowed_source_file_extensions = tuple(allowed_source_file_extensions)

        if self.invalid_file_extension(filename):
            raise ValueError("Invalid file extension")

        self.open_loop_symbol = open_loop_symbol
        self.closed_loop_symbol = closed_loop_symbol
        
        with open(filename, "r", encoding = "utf-8") as source_code_file:
            self.source_code = source_code_file.read()

        # The key is the memory cell index, the value is the value inside the cell
        self.memory = {0 : 0}

        self.closed_brackets = {}
        self.open_brackets = {}

        if self.loop_symbols_defined():
            self.setup_bracket_dicts()

    def invalid_file_extension(self, filename):
        return not filename.endswith(self.allowed_source_file_extensions)

    def loop_symbols_defined(self):
        return self.open_loop_symbol != None and self.closed_loop_symbol != None

    def setup_bracket_dicts(self):
        brackets = []
        i = 0

        while i < len(self.source_code):
            if self.source_code[i] == self.open_loop_symbol:
                brackets.append(i)

            elif self.source_code[i] == self.closed_loop_symbol:
                b = brackets.pop()
                self.closed_brackets[b] = i
                self.open_brackets[i] = b
                
            i += 1
