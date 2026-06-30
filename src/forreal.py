import argparse

from src.interpreters.forreal_interpreter import ForrealInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str)
    args = parser.parse_args()
    ForrealInterpreter(args.source_code_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
