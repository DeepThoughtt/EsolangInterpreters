import argparse

from src.interpreters.smallfuck_interpreter import SmallfuckInterpreter

def main():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument("source_code_file", type = str)
    parser.add_argument("data_file", type = str)
    args = parser.parse_args()
    result_tape = SmallfuckInterpreter(args.source_code_file, args.data_file).run()
    print(result_tape, end = "")

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
