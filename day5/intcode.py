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
    def jump_if_true(self, ptr, program, mode):
        a = int(program[ptr[0]+1])
        b = int(program[ptr[0]+2])
        if (int(program[a]) if mode[-1] == "0" else a) != 0:
            ptr[0] = int(program[b]) if mode[-2] == "0" else b
        else:
            ptr[0] += 3

    # Opcode 6
    def jump_if_false(self, ptr, program, mode):
        a = int(program[ptr[0]+1])
        b = int(program[ptr[0]+2])
        if (int(program[a]) if mode[-1] == "0" else a) == 0:
            ptr[0] = int(program[b]) if mode[-2] == "0" else b
        else:
            ptr[0] += 3

    # Opcode 7
    def less_than(self, ptr, program, mode):
        a = int(program[ptr+1])
        b = int(program[ptr+2])
        if (int(program[a]) if mode[-1] == "0" else a) < (int(program[b]) if mode[-2] == "0" else b):
            program[int(program[ptr+3])] = 1
        else:
            program[int(program[ptr+3])] = 0

    # Opcode 8
    def equals(self, ptr, program, mode):
        a = int(program[ptr+1])
        b = int(program[ptr+2])
        if (int(program[a]) if mode[-1] == "0" else a) == (int(program[b]) if mode[-2] == "0" else b):
            program[int(program[ptr+3])] = 1
        else:
            program[int(program[ptr+3])] = 0

    def opcode(self, p, program):
        ptr = p[0]
        code = program[ptr][-2:]
        mode = program[ptr][:-2]
        for i in range(3 - len(mode)):
            mode = "0" + mode
        if code == "99":
            print("HALT")
            #print(program)
            exit()
        elif code == "1" or code == "01":
            self.add(ptr, program, mode)
            p[0] += 4
        elif code == "2" or code == "02":
            self.multiply(ptr, program, mode)
            p[0] += 4
        elif code == "3" or code == "03":
            self.store(5, ptr, program, mode)
            p[0] += 2
        elif code == "4" or code == "04":
            out = self.output(ptr, program, mode)
            print("output: " + str(out))
            p[0] += 2
        elif code == "5" or code == "05":
            self.jump_if_true(p, program, mode)
        elif code == "6" or code == "06":
            self.jump_if_false(p, program, mode)
        elif code == "7" or code == "07":
            self.less_than(ptr, program, mode)
            p[0] += 4
        elif code == "8" or code == "08":
            self.equals(ptr, program, mode)
            p[0] += 4

    def run(self):
        i = [0]
        while i[0] < len(self.program):
            self.opcode(i, self.program)
    