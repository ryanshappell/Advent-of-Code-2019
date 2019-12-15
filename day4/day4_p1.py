min = "145852"
max = "616942"
curr = min

def check(val):
    double = False
    for i in range(len(val)-1):
        if val[i] == val[i+1]:
            double = True
        if val[i] > val[i+1]:
            return False
    return double

count = 0
while int(curr) < int(max):
    if check(curr):
        count += 1
    curr = str(int(curr) + 1)

print(count)
