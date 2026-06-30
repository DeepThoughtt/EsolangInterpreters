import argparse

from src.interpreters.brainfuck_interpreter import BrainfuckInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str)
    args = parser.parse_args()
    BrainfuckInterpreter(args.source_code_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
