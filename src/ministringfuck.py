import argparse

from src.interpreters.ministringfuck_interpreter import MiniStringFuckInterpreter

def main():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument("source_code_file", type = str)
    args = parser.parse_args()
    MiniStringFuckInterpreter(args.source_code_file).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
