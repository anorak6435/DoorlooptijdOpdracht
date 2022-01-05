from graph import GraphNode, Graph

if __name__ == '__main__':
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

    # maak een topoligische sortering van de nodes in de graaf
    graaf.sortNodes()
    print("Doorlooptijd project:", graaf.ShortestTimeDone())

