import argparse

from src.interpreters.paintfuck_interpreter import PaintfuckInterpreter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_code_file", type = str)
    parser.add_argument("-i", "--iterations", type = int)
    parser.add_argument("-w", "--width", type = int)
    parser.add_argument("-h", "--height", type = int)
    args = parser.parse_args()
    PaintfuckInterpreter(args.source_code_file, args.iterations, args.width, args.height).run()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
