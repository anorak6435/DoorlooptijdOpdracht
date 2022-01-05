from graph import GraphNode, Graph
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Jarno')


    # maak graphnodes
    a = GraphNode("A", 6, [])
    b = GraphNode("B", 3, [])
    c = GraphNode("C", 4, [a])
    d = GraphNode("D", 10, [b])
    e = GraphNode("E", 7, [b,c])
    f = GraphNode("F", 8, [a])
    g = GraphNode("G", 8, [e,f])

    # Dependencies: key heeft lijst aan nodes afhankelijk van hem
    deps = {
        a: [c, f],
        b: [d, e],
        c: [e],
        d: [],
        e: [g],
        f: [g],
        g: []
    }

    # maak graph
    graaf = Graph([a, b, c, d, e, f, g], deps)

    print(graaf)

    graaf.sortNodes()

    graaf.printMoments()
    # graaf.restoreDependency() # prob don't need to do that anymore

    # geef de dictionary van depencencies mee en een lijst van beschikbare nodes. Die leeg begint.
    print("Doorlooptijd project:", graaf.ShortestTimeDone())

