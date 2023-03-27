from .Node import Node
from typing import List

class Tree:
    
    root: Node
    
    def __init__(self, root: Node) -> None:
        self.root = root
        
    def is_value_present(self, value):
        return self.root.is_value_present(value=value)
    
    def find_leaf_for_insertion(self, value):
        way = self.getWay()
        self.insert_value_in_node(way=way, value=value, node_offset=0)        
        
    
    def getWay(self, value) -> List[int]:
        node: Node = self.root
        way: List[int] = []
        
        while True:
            if len(node.children) == 0:
                break
                
            if len(node.values) == 1:
                node = node.children[0] if node.values[0] > value else node.children[1]
                
            elif len(node.values) == 2:
                if value < node.values[0]:
                    node = node.children[0]
                    way.append(0)
                    
                elif value > node.values[1]:
                    node = node.children[2]
                    way.append(2)
                    
                else:
                    node = node.children[1]
                    way.append(1)

        return way            
        
        
    def insert_value_in_node(self, way: List[Node], value: int, node_offset: int):
        node = None
        if len(way) != 0:
            node = way[len(way)-1-node_offset]
        else:
            node = self.root
            
        if len(node.values) == 1:
            node.values.append(value)
        
        elif len(node.values) == 2:
            if node != self.root:
                self.insert_value_in_node(way=way, value=value, node_offset=node_offset+1)
            else:
                values = node.values
                values.append(value)
                values.sort()
                left_node = Node(values[0])
                right_node = Node(value[2])
                self.root = Node([1], [left_node, right_node])
            
            