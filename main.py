
#%%

import networkx as nx
from models import *
# class crossroad:


with open('a.txt', 'r') as inputfile:

    counter = 0
    car_id = 0
    streets = {}
    cars = {}

    for line in inputfile.readlines():
        if counter == 0:
            duration, intersections, number_streets, number_cars, bonus = line.replace('\n','').split(' ')
            number_streets = int(number_streets)
            first_line = False

        elif counter <= number_streets:
            start_intersection, end_intersection, name, length = line.replace('\n', '').split(' ')
            streets[name] = {'from': int(start_intersection), 'to': int(end_intersection), 'length': int(length)}
        else:
            car_path = line.replace('\n', '').split(' ')
            print(type(cars))
            cars[car_id] = car_path[1:]
            car_id += 1

        counter += 1
        # streets[name] = [start_intersection, end_intersection, length]

niceCity = City(streets, int(intersections), cars)

niceCity.draw()
