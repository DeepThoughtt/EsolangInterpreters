import argparse

from src.interpreters.boolfuck_interpreter import BoolfuckInterpreter

def main():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument("source_code_file", type = str)
    args = parser.parse_args()
    BoolfuckInterpreter(args.source_code_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
