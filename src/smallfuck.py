import argparse

from src.interpreters.smallfuck_interpreter import SmallfuckInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str, required = True)
    parser.add_argument("data_file", type = str, required = True)
    args = parser.parse_args()
    SmallfuckInterpreter(args.source_code_file, args.data_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
