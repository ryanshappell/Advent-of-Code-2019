file = open("day1_input.txt", "r")

def calc_fuel(amount):
    amount = int(amount)
    temp = (int) (amount / 3) - 2
    if temp <= 0:
        return amount
    else:
        amount += calc_fuel(temp)
    return amount

fuel = 0
for mass in file:
    fuel += calc_fuel(mass) - int(mass)
print(fuel)
file.close()
