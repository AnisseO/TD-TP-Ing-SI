from typing import List
from .Node import Node

class Node:
    
    values: List[int] = []
    children: List[Node] = []
    
    def __init__(self, values, children) -> None:
        self.values = values
        self.children = children
    
    def is_leaf(self) -> bool:
        return len(self.children)  == 0
    
    def is_value_present(self, value: int):
        if value in self.values:
            return True
        else:
            for child in self.children:
                if child.is_value_present(value):
                    return True
        return False
    
    