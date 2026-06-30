import argparse

from src.interpreters.minibitmove_interpreter import MiniBitMoveInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str)
    parser.add_argument("data_file", type = str)
    args = parser.parse_args()
    MiniBitMoveInterpreter(args.source_code_file, args.data_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
