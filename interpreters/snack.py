class SnackInterpreter:

    def __init__(self, program):
        self.program_commands = program.split("\n")
        
    
    def run(self):
        out = ""
        eat = 0
        
        for command in self.program_commands:
            if command == "grave":
                eat = 0
            elif command == "get":
                eat += 1
            elif command == "let":
                eat -= 1
            elif command == "slime":
                out += "Your victims look crazy and awful. They are afraid of you\n"
            elif command == "eat":
                out += f"You have eaten as a snack right {eat} people. Happy?\n"
                eat = 0
            elif command == "sleep":
                out += "SLEEP? ARE YOU CRAZY? LETS GET UP FOR MIDNIGHT DINNER\n"
        
        if len(out) > 0:
            out = out[0 : len(out) - 1]
            
        return out
    