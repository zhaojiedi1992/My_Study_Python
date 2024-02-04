class Node(object): 
    def __init__(self,value) -> None:
        self._value = value
        self._child = [ ]
    
    def __repr__(self) -> str:
        return 'Node({!r})'.format(self._value)

    def add_child(self,node):
        self._child.append(node)

    def __iter__(self):
        return iter(self._child)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    # def width_first(self):
    #     # yield self
    #     yield from self._child
    #     for c in self:
    #         yield from c.width_first()

class NodeV2(object):
    def __init__(self,value) -> None:
        self._value = value
        self._child = [ ]
    
    def __repr__(self) -> str:
        return 'Node({})'.format(self._value)

    def add_child(self,node):
        self._child.append(node)

    def __iter__(self):
        return iter(self._child)
    def depth_first(self):
        return DepthFirstIterator(self)
    
# todo DepDepthFirstIterator


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

#            0
#         1      2
#       3  4   5
# 
    for ch in root.depth_first():
        print(ch)
    print('-'*20)
    # for ch in root.width_first():
    #     print(ch)

    
