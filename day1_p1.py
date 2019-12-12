file = open("day1_input.txt", "r")
fuel = 0
for mass in file:
    fuel += (int) (int(mass) / 3) - 2
print(fuel)
file.close()
