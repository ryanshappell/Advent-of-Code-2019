import datetime

print(datetime.datetime.now())
file = open("day3/day3_input.txt", "r")
wire1 = file.readline().split(",")
wire2 = file.readline().split(",")

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.zero = False
        if x == 0 and y == 0:
            self.zero = True

    def pCoord(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def createLine(pos, val, dir):
    line = []
    line.append(Coord(pos.x, pos.y))
    for i in range(1, val+1):
        if dir == "U":
            line.append(Coord(pos.x, pos.y + i))
        elif dir == "D":
            line.append(Coord(pos.x, pos.y - i))
        elif dir == "L":
            line.append(Coord(pos.x - i, pos.y))
        elif dir == "R":
            line.append(Coord(pos.x + i, pos.y))
    return line

def getLines(array):
    lines = []
    curr_pos = Coord(0, 0)
    i = 0
    while i < len(array):
        dir = array[i][0]
        val = int(array[i][1:])
        lines.append(createLine(curr_pos, val, dir))
        if dir == "U":
            curr_pos.y += val
        elif dir == "D":
            curr_pos.y -= val
        elif dir == "L":
            curr_pos.x -= val
        elif dir == "R":
            curr_pos.x += val
        i += 1
    return lines

def intersect(line1, line2):
    p1 = 0
    p2 = 0
    for coord1 in line1:
        for coord2 in line2:
            if coord1.x == coord2.x and coord1.y == coord2.y:
                return coord1, p1, p2
            p2 += 1
        p2 = 0
        p1 += 1
    return Coord(0, 0), 0, 0

def getIntersections(wire1, wire2):
    paths = []
    distances = []
    path1 = 0
    path2 = 0
    for line1 in wire1:
        for line2 in wire2:
            if (line1[0].x == line1[-1].x and line2[0].x == line2[-1].x) or (line1[0].y == line1[-1].y and line2[0].y == line2[-1].y):
                path2 += len(line2) - 1
                continue
            cross, p1, p2 = intersect(line1, line2)
            if not cross.zero:
                paths.append(path1 + p1 + path2 + p2)
                distances.append(abs(cross.x) + abs(cross.y))
            path2 += len(line2) - 1
        path2 = 0
        path1 += len(line1) - 1
    return min(paths), min(distances)

wire1 = getLines(wire1)
wire2 = getLines(wire2)
path, distance = getIntersections(wire1, wire2)
print("Minimum Dist: " + str(distance))
print("Minumum Path: " + str(path))

print(datetime.datetime.now())
file.close()
