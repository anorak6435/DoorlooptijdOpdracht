class GraphNode:
    def __init__(self, _name, _duration, _dependant):
        self.name = _name
        self.duration = _duration
        self.depending = _dependant

    def __repr__(self):
        return "".join(["Node(", str(self.name), ", ", str(self.duration), ")"])

class Graph:
    def __init__(self, _nodes):
        self.moment = _nodes
        # self.moment [
        #     [],
        #     [] # etc...
        # ]

    def __repr__(self):
        return str(self.moment)
