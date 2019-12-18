class Intcode():
    def __init__(self, file):
        self.file = open(file, "r")
        self.program = self.file.read().split(",")

    # Opcode 1
    def add(self, ptr, program, mode):
        a = int(program[ptr+1])
        b = int(program[ptr+2])
        program[int(program[ptr+3])] = str((int(program[a]) if mode[-1] == "0" else a) + (int(program[b]) if mode[-2] == "0" else b))

    # Opcode 2
    def multiply(self, ptr, program, mode):
        a = int(program[ptr+1])
        b = int(program[ptr+2])
        program[int(program[ptr+3])] = str((int(program[a]) if mode[-1] == "0" else a) * (int(program[b]) if mode[-2] == "0" else b))

    # Opcode 3
    def store(self, in_val, ptr, program, mode):
        program[int(program[ptr+1])] = str(in_val)

    # Opcode 4
    def output(self, ptr, program, mode):
        a = int(program[ptr+1])
        return int(program[a]) if mode[-1] == "0" else a
    
    # Opcode 5
    def jump_if_true(self):
        pass

    # Opcode 6
    def jump_if_false(self):
        pass

    # Opcode 7
    def less_than(self):
        pass

    # Opcode 8
    def equals(self):
        pass

    def opcode(self, p, program):
        ptr = p[0]
        code = program[ptr][-2:]
        mode = program[ptr][:-2]
        for i in range(3 - len(mode)):
            mode = "0" + mode
        if code == "99":
            print("HALT")
            exit()
        elif code == "1" or code == "01":
            self.add(ptr, program, mode)
            p[0] += 4
        elif code == "2" or code == "02":
            self.multiply(ptr, program, mode)
            p[0] += 4
        elif code == "3" or code == "03":
            self.store(1, ptr, program, mode)
            p[0] += 2
        elif code == "4" or code == "04":
            out = self.output(ptr, program, mode)
            print("output: " + str(out))
            p[0] += 2
        elif code == "5" or code == "05":
            pass
        elif code == "6" or code == "06":
            pass
        elif code == "7" or code == "07":
            pass
        elif code == "8" or code == "08":
            pass


    def run(self):
        i = [0]
        while i[0] < len(self.program):
            self.opcode(i, self.program)
    