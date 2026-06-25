from src.base.esolang_interpreter import EsolangInterpreter

class BoolfuckInterpreter(EsolangInterpreter):

    def __init__(self, filename, input_chars):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".bfk"],
            open_loop_instruction = "[",
            closed_loop_instruction = "]",
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
        )

        self.input_bytes_list = []
        self.output_bits_list = []
        self.fill_input_bits_lists(input_chars)
        self.language_instructions[";"] = self.print_to_output_list
        self.language_instructions[","] = self.read_bit_from_input
        self.language_instructions["+"] = self.flip_bit

    def flip_bit(self):
        if self.memory[self.memory_pointer] == 0:
            self.memory[self.memory_pointer] = 1
        else:
            self.memory[self.memory_pointer] = 0

    def read_bit_from_input(self):
        # No more bits to read, put a 0 in the pointed memory cell
        if len(self.input_bytes_list) == 0:
            self.memory[self.memory_pointer] = 0
            return
        
        # Else read a bit from the input in little endian mode
        self.memory[self.memory_pointer] = self.input_bytes_list[0].pop()

        # If there are no more bits to read in this byte delete it
        if len(self.input_bytes_list[0]) == 0:
            del self.input_bytes_list[0]

    def print_to_output_list(self):
        # We read the bit in the memory cell pointed and add it to the output
        read_bit = self.memory[self.memory_pointer]
        self.output_bits_list.insert(0, read_bit)

        # If we reach one byte of length for the output
        # list we print it out and then clear it
        if len(self.output_bits_list) == 8:
            char_bits = map(str, self.output_bits_list)
            self.output_bits_list.clear()
            out_char = "".join(char_bits)
            print(out_char)

    def fill_input_bits_lists(self, input_chars):
        # We convert the input characters in lists of bits
        for character in input_chars:
            char_bits = bin(ord(character))[2:].zfill(8)
            self.input_bytes_list.append(int(bit) for bit in char_bits)
