

class crossroad:


with open('a.txt', 'r') as inputfile:
    first_line = inputfile.readline()
    duration, intersections, streets, cars, bonus = first_line.split(' ')

