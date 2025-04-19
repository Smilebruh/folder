#! /usr/bin/python3

from __future__ import annotations
import os 

class GeneralTree():
    def  __init__(self, path: str = "."):
        self.path: str = path
        self.folder: list[GeneralTree] = []
    
    def add(self, folder: GeneralTree):
        self.folder.append(folder)

    def make_tree(self, path=".", obj = None):
        #BFS (Breadth-First-Searching)
        if not obj:
            obj = self

        for dir in [i for i in os.listdir(path) if os.path.isdir(os.path.join(path,i))]:
            tree = GeneralTree(path=os.path.join(path,dir))
            obj.add(tree)
            
            for chdir in [i for i in os.listdir(tree.path) if os.path.isdir(os.path.join(tree.path, i))]:
                childir = GeneralTree(path=os.path.join(tree.path, chdir))
                tree.add(childir)
            
                obj.make_tree(path=childir.path,obj = childir)


    def print_all(self, obj: GeneralTree = None):
        #DFS (Depth-First-Searching)
        if not obj:
            obj = self
        
        for folder in obj.folder:
            print(folder.path)
            self.print_all(folder)
            


# Test
if __name__ == "__main__":
    x = GeneralTree()
    x.make_tree()

    print([i.path for i in x.folder])
    x.print_all()
