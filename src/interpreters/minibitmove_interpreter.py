from src.base.esolang_interpreter import EsolangInterpreter

class MiniBitMoveInterpreter(EsolangInterpreter):

    def __init__(self, filename, data_file):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".mbm"],
        )

        if not data_file.endswith(".mbmdata"):
            raise ValueError("Invalid data file extension")

        with open(data_file, "r", encoding = "utf-8") as data_file:
            file_content = data_file.read()

            for i in range(len(file_content)):
                self.memory[i] = int(file_content[i])
        
    def run(self):
        while self.memory_pointer < len(self.memory):
            if self.source_code[self.source_code_pointer] == "1":
                self.flip_bit()

            elif self.source_code[self.source_code_pointer] == "0":
                self.memory_pointer += 1

            self.source_code_pointer = (self.source_code_pointer + 1) % len(self.source_code)

        return "".join(str(bit) for bit in self.memory.values())
