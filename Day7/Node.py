from __future__ import annotations

class Node:
    def __init__(self, isDirectory: bool, name: str = "", value: int = 0, parent: Node = None) -> None:
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []
        self.isDirectory = isDirectory
    
    def AddChild(self, name: str, value: int) -> None:
        child = Node(name, value)
        child.parent = self
        self.children.append(child)
    
    def AddChild(self, child: Node) -> None:
        child.parent = self
        self.children.append(child)
    
    def __repr__(self) -> str:
        return f'(Name=\"{self.name}\", Value={self.value}, Parent=\"{self.parent.name if self.parent is not None else "None"}\")'
