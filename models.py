import networkx as nx
from typing import Tuple, Dict, List

@dataclass
class CarState:
    street: str
    time_left: int

class Vertex:
    
        
@dataclass
class City:
    state: Dict[int, CarState]
    
    def __init__(self, 
                 streets: List[Dict[str, int]], 
                 intersections: int, 
                 paths: Dict[int, List[str]]):
        self.state = {}
        for car, path in paths.items():
            self.state[car] = CarState(path[0], 0)
        
        
        
        