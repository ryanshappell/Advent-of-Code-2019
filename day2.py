file = open("day2_input.txt", "r")
data = list(map(int, file.read().split(",")))

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
print(data)
file.close()
