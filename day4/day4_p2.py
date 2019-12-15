min = "145852"
max = "616942"
curr = min

def check(val):
    doubles = []
    checked = []
    for i in range(len(val)-1):
        if val[i] > val[i+1]:
            return False
        if val[i] == val[i+1]:
            if val[i] in doubles:
                doubles.remove(val[i])
            elif val[i] not in checked:
                checked.append(val[i])
                doubles.append(val[i])
    return len(doubles) > 0

count = 0
while int(curr) < int(max):
    if check(curr):
        count += 1
    curr = str(int(curr) + 1)

print(count)
