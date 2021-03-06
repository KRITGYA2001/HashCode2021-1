import networkx as nx
from dataclasses import dataclass, field
from typing import Tuple, Dict, List
import matplotlib.pyplot as plt

@dataclass
class CarState:
    street_index: int
    time_left: int

@dataclass
class Intersection:
    incoming_streets: Dict[str, bool] = field(default_factory=dict)
    order: List[str] = field(default_factory=list)
    
    def set_green(self, step):
        turn_off = self.order[step % len(self.order)]
        turn_on = self.order[(step + 1) % len(self.order)]
        self.incoming_streets[turn_off] = False
        self.incoming_streets[turn_on] = True


class City:

    def __init__(self, steps, streets, number_of_intersections, paths, test_case):

        self.steps = steps
        self.paths = paths
        self.streets = streets
        self.state = {}
        self.intersections = {}
        self.G = nx.DiGraph()
        self.test_case = test_case

        for car, path in paths.items():
            self.state[car] = CarState(0, 0)

        
        for inter in range(number_of_intersections):
            self.intersections[inter] = Intersection()
        
        for street_name, street in streets.items():
            self.intersections[street["to"]].incoming_streets[street_name] = False
            self.intersections[street["to"]].order.append(street_name)

            self.G.add_edge(street["from"], street["to"], weight = street["length"])
            
        for node in self.G.nodes:
            self.G.nodes[node]["inter"] = self.intersections[node]
            
            
    def output(self):
        lines = [str(len(self.intersections))]
        for key, intersection in self.intersections.items():
            lines.append(str(key))
            lines.append(str(len(intersection.incoming_streets)))
            for key in intersection.incoming_streets:
                lines.append(f"{key} 1")
        with open(f"{self.test_case}.out", "w") as out:
            out.write("\n".join(lines))
            
