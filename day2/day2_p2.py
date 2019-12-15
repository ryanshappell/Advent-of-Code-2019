file = open("day2/day2_input.txt", "r")
original = file.read()
orig_data = list(map(int, original.split(",")))
file.close()

def reset():
    file = open("day2_input.txt", "w")
    file.write(original)
    file.close()
    
def check(noun, verb):
    file = open("day2_input.txt", "r")
    data = list(map(int, file.read().split(",")))

    data[1] = noun
    data[2] = verb

    i = 0
    while i < len(data):
        if data[i] == 99:
            break
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i += 3
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i += 3
        i += 1
    file.close()
    reset()
    return data[0]

for noun in range(100):
    for verb in range(100):
        if check(noun, verb) == 19690720:
            print("FOUNDDD")
            print(str(100 * noun + verb))
            break
