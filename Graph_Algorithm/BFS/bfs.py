
adjList = {}

visited ={}

with open('input.txt') as f:
    edges = int(f.readline())
    for i in range(edges):
        lineStr = f.readline().split(' ')
        fromNode , toNode = int(lineStr[0]), int(lineStr[1])
        adjList[fromNode] = []
        adjList[toNode] = []

with open('input.txt') as f:
    edges = int(f.readline())
    for i in range(edges):
        lineStr = f.readline().split(' ')
        fromNode , toNode = int(lineStr[0]), int(lineStr[1])
        adjList[fromNode].append(toNode)
        adjList[toNode].append(fromNode)
        visited[fromNode] = False
        visited[toNode] = False




def BFS(startNode):
    visitedSeq = []
    q = []
    q.append(startNode)
    visited[startNode] = True
    while q:
        frontNode = q.get()
        for neighbour in adjList[frontNode]:
            if not visited[neighbour]:
                q.put(neighbour)
                visited[neighbour] = True
                visitedSeq.append(neighbour)

        return visitedSeq
print(BFS(0))



