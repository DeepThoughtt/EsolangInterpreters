from src.base.esolang_interpreter import EsolangInterpreter

class BoolfuckInterpreter(EsolangInterpreter):

    def __init__(self, filename):

        super().__init__(
            filename = filename,
            allowed_source_file_extensions = [".bfk"],
            open_loop_instruction = "[",
            closed_loop_instruction = "]",
            move_pointer_left_instruction = "<",
            move_pointer_right_instruction = ">",
            flip_bit_instruction = "+",
        )

        self.add_instruction(";", self.print_to_output_list)
        self.add_instruction(",", self.read_bit_from_input)
        self.output_buffer = []
        self.input_buffer = []

    def read_bit_from_input(self):
        # No more bits to read, read input from the user
        if len(self.input_buffer) == 0:
            input_char = input()

            if len(input_char) != 0:
                char_bits = bin(ord(input_char[0]))[2:].zfill(8)
                self.input_buffer.append(int(bit) for bit in char_bits)
            else:
                self.input_buffer.append(0)

        # Now we read a bit from the input buffer in little endian mode
        self.memory[self.memory_pointer] = self.input_buffer.pop()

    def print_to_output_list(self):
        # We read the bit in the pointed memory cell and add it to the output
        read_bit = self.memory[self.memory_pointer]
        self.output_buffer.insert(0, read_bit)

        # If we reach one byte of length for the output
        # list we print it out and then clear it
        if len(self.output_buffer) == 8:
            char_bits = [str(bit) for bit in self.output_buffer]
            out_char = "".join(char_bits)
            self.output_buffer.clear()
            print(out_char)
