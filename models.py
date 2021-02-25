import networkx as nx
from dataclasses import dataclass, field
from typing import Tuple, Dict, List
import matplotlib.pyplot as plt

@dataclass
class CarState:
    street: str
    time_left: int

@dataclass
class Intersection:
    incoming_streets: Dict[str, bool] = field(default_factory=dict)
    
        
@dataclass
class City:
    G: nx.DiGraph
    state: Dict[int, CarState]
    intersections: Dict[int, Intersection]
    streets: Dict[str, Dict[str, int]]
    
    def __init__(self, 
                 streets: Dict[str, Dict[str, int]], 
                 intersections: int, 
                 paths: Dict[int, List[str]]):
        self.state = {}
        self.G = nx.DiGraph()
        for car, path in paths.items():
            self.state[car] = CarState(path[0], 0)
        
        for inter in range(intersections):
            self.intersections[inter] = Intersection()
        
        for street_name, street in streets.items():
            self.intersections[street["to"]].incoming_streets[street_name] = False
            self.G.add_edge(street["from"], street["to"], weight = street["length"])
            
        for node in self.G.nodes:
            self.G.nodes[node]["inter"] = self.intersections[node]
            
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()
        
