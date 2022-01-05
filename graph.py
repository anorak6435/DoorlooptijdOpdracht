class GraphNode:
    def __init__(self, _name, _duration, _dependant):
        self.name = _name
        self.duration = _duration
        self.voorgangers = _dependant

    def hasDependency(self):
        return len(self.voorgangers) > 0

    def __repr__(self):
        return "".join(["Node(", str(self.name), ", ", str(self.duration), ")"])


class Graph:
    def __init__(self, _nodes, deps):
        self.moment = [_nodes]
        self.dependencies = deps
        # self.moment [
        #     [],
        #     [] # etc...
        # ]

    def __repr__(self):
        return str(self.moment)

    def sortNodes(self, index=0):
        # loop achterste voren over de nodes lijst omdat nodes die dependencies hebben uit deze lijst worden verwijderd
        # niet van 0 naar lengte zou ik nodes overslaan.
        for x in range(len(self.moment[index])-1, -1, -1):
            node = self.moment[index][x]
            # als de node een dependency heeft: zet de node in de volgende lijst.
            if node.hasDependency():
                self.moveNodeDown(node, index)

        # Als dit niet de laatste lijst is
        if not self.isLastList(index):
            # update voorgangers
            self.updateDependency(self.moment[index], self.moment[index + 1])
            self.sortNodes(index+1)  # zo niet sorteer volgende lijst

    # debug print de lijsten van momenten regel voor regel
    def printMoments(self):
        for moment in self.moment:
            print(moment)

    # is de rowindex the index van de laatste lijst
    def isLastList(self, rowindex):
        return rowindex + 1 == len(self.moment)

    # in de huidige rij staat een node die een rij omlaag kan, omdat hij dependencies heeft.
    # rijen worden toegevoegd wanneer ze nodig zijn.
    def moveNodeDown(self, node, rowindex):
        # Als deze index van de laatste rij is moet er een extra rij toegevoegd worden
        if self.isLastList(rowindex):
            self.moment.append([])
        self.moment[rowindex + 1].append(node)
        self.moment[rowindex].remove(node)

    # haal de dependencies die in de gesorteerde lijst voorkomen uit de ongesorteerde lijst.
    def updateDependency(self, gesorteerde_activiteiten, ongesorteerde_activiteiten):
        for activiteit in ongesorteerde_activiteiten:
            # ga achterstevoren over de lijst omdat tijdens de loop items verwijderd worden
            for x in range(len(activiteit.voorgangers)-1, -1, -1):
                voortganger = activiteit.voorgangers[x]
                if voortganger in gesorteerde_activiteiten:
                    activiteit.voorgangers.remove(voortganger)

    def ShortestTimeDone(self):
        # van achter naar voren over de nodes met for loop.
        for momentIndex in range(len(self.moment)-1, -1, -1):
            for i in range(len(self.moment[momentIndex])):
                # de visit functie past de duration aan om de doorlooptijd te vinden.
                self.moment[momentIndex][i] = self.visit(self.moment[momentIndex][i])
        # hier zijn we door alle momenten gegaan. De hoogste waarde van het eerste moment is de langste doorlooptijd
        return max(self.moment[0][0].duration, self.moment[0][1].duration)

    # De visit functie heeft 3 interessante cases om te controleren
    # als geen latere node op deze node depends
    # als één latere node op deze node depends voeg de tijd van de latere node toe.
    # als twee later nodes op deze node dependen voeg de langste tijd van de latere node toe.
    def visit(self, node):
        # controleer of deze node nodes heeft die afhankelijk zijn van hem
        if len(self.dependencies[node]) == 0:
            return node  # node heeft geen latere afhankelijkheden dus er gebeurt niets met zijn waarde
        elif len(self.dependencies[node]) == 1:
            # voeg de depenceny duration toe aan de duration van deze node
            node.duration += self.dependencies[node][0].duration
            return node
        elif len(self.dependencies[node]) == 2:
            # voeg de hoogste dependency duration toe aan de duration van deze node
            node.duration += max(self.dependencies[node][0].duration, self.dependencies[node][1].duration)
            return node



