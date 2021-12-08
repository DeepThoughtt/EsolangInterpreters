# Esolang-Interpreters
A collection of interpreters for esoteric languages

## What is an esoteric language?
An esoteric programming language is a programming language designed to test the boundaries of computer programming language design, 
as a proof of concept, as software art, as a hacking interface to another language, or as a joke (more info [here](https://en.wikipedia.org/wiki/Esoteric_programming_language)).

## How do I use the interpreters?
To use an interpreter import the module in your program and then pass the needed parameters to the interpreter's constructor and execute the `run()` function, this will
give you the result for the program you wrote. For example:

```
from MiniBitMoveInterpreter import MiniBitMoveInterpreter
result = MiniBitMoveInterpreter('10', '1100101').run()
print(result) # "0011010"
```

## What languages can be interpreted?
- [4RL](https://esolangs.org/wiki/4RL)
- [ABCD](https://esolangs.org/wiki/ABCD)
- [Boolfuck](https://esolangs.org/wiki/Boolfuck)
- [Brainfuck](https://esolangs.org/wiki/Brainfuck)
- [InfiniTick](https://esolangs.org/wiki/InfiniTick)
- [MiniBitMove](https://esolangs.org/wiki/MiniBitMove)
- [MiniStringFuck](https://esolangs.org/wiki/MiniStringFuck)
- [Paintfuck](https://esolangs.org/wiki/Paintfuck)
- [Smallfuck](https://esolangs.org/wiki/Smallfuck)
- [Tick](https://esolangs.org/wiki/Tick)
- Ticker (no info found)
