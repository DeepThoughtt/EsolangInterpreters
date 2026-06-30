import pathlib

from src.base.esolang_interpreter import EsolangInterpreter

class MiniBitMoveInterpreter(EsolangInterpreter):

    def __init__(self, source_code_file, data_file):

        super().__init__(
            source_code_file = source_code_file,
            allowed_source_file_extensions = [".mbm"],
        )

        data_file_path = pathlib.Path(data_file)

        if not data_file_path.is_file():
            raise ValueError("File not found")

        if not data_file.endswith(".mbmdata"):
            raise ValueError("Invalid data file extension")

        # MiniBitMove requires a source code file and a data file
        with open(data_file, "r", encoding = "utf-8") as data_file_content:
            file_content = data_file_content.read()

            for i in range(len(file_content)):
                if file_content[i] == "0" or file_content[i] == "1":
                    self.memory[i] = ord(file_content[i])
        
    def run(self):
        # The code keeps running until the end of the data is reached
        while self.memory_pointer < len(self.memory):
            if self.source_code[self.source_code_pointer] == "1":
                self.flip_bit()

            elif self.source_code[self.source_code_pointer] == "0":
                self.memory_pointer += 1

            self.source_code_pointer = (self.source_code_pointer + 1) % len(self.source_code)

        return "".join(str(bit) for bit in self.memory.values())
