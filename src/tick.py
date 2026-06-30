import argparse

from src.interpreters.tick_interpreter import TickInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str, required = True)
    args = parser.parse_args()
    TickInterpreter(args.source_code_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
