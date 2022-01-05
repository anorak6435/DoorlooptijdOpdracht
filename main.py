from graph import GraphNode, Graph, Dependency
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Jarno')

    # Dependency's
    deps = {
        "C": [Dependency("C", "A")],
        "D": [Dependency("D", "B")],
        "E": [Dependency("E", "B"), Dependency("E", "C")],
        "F": [Dependency("F", "A")],
        "G": [Dependency("G", "E"), Dependency("G", "F")]
    }
    # maak graphnodes
    a = GraphNode("A", 6, [])
    b = GraphNode("B", 3, [])
    c = GraphNode("C", 4, [a])
    d = GraphNode("D", 10, [b])
    e = GraphNode("E", 7, [b,c])
    f = GraphNode("F", 8, [a])
    g = GraphNode("G", 8, [e,f])

    # maak graph
    graaf = Graph([a, b, c, d, e, f, g])

    print(graaf)

    graaf.sortNodes()

    graaf.printMoments()
    # graaf.restoreDependency() # prob don't need to do that anymore

    graaf.ShortestTimeDone(deps)