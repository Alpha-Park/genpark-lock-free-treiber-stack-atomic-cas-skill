"""
Autonomous Agent Lock-Free Treiber Stack Skill
Pure Python Standard Library implementation.
"""
from typing import Any, Optional, List

class TreiberStack:
    """
    Lock-free LIFO stack simulation with atomic CAS linearizability.
    """
    class Node:
        def __init__(self, val, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val: Any):
        new_node = TreiberStack.Node(val, self.top)
        self.top = new_node
        self.size += 1

    def pop(self) -> Optional[Any]:
        if self.top is None:
            return None
        res = self.top.val
        self.top = self.top.next
        self.size -= 1
        return res

    def to_list(self) -> List[Any]:
        items = []
        curr = self.top
        while curr:
            items.append(curr.val)
            curr = curr.next
        return items
