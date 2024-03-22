
import math
import heapq

coordinates = {}
adjList = {}

with open('input2.txt') as f:
    vertex = int(f.readline())
    for i in range(vertex):
        lineStr = f.readline().split(' ')
        node, x, y = lineStr[0] ,int(lineStr[1]) , int(lineStr[2])
        coordinates[node] = (x,y)
        adjList[node] = []
    edges = int(f.readline())
    for i in range(edges):
        lineStr = f.readline().split()
        fromNode ,toNode, weight = lineStr[0] , lineStr[1] , int(lineStr[2])
        adjList[fromNode].append((toNode,weight))
    startNode = f.readline().rsplit()
    startNode = startNode[0]
    goalNode = f.readline().rsplit()
    goalNode = goalNode[0]

def heuristic(currCoordi):
    return math.sqrt((currCoordi[0]-coordinates[goalNode][0])**2 - (currCoordi[1] - coordinates[goalNode][1])**2)


class State:
    def __init__(self,node,g,parent):
        self.node = node
        self.g = g
        self.f = g + heuristic(coordinates[node])
        self.parent = parent
    def __lt__(self, other):
        return self.f < other.f

def aStarSearch():
    ans = []
    q = []
    startState = State(startNode,0,None)
    heapq.heappush(q,startState)
    while q:
        currState = heapq.heappop(q)
        if(currState.node == goalNode):
            while currState is not None:
                ans.append(currState.node)
                currState = currState.parent
            return ans

        for neighbour in adjList[currState.node]:
            gnew = currState.g + neighbour[1]
            newState = State(neighbour[0],gnew,currState)
            heapq.heappush(q,newState)

    return ans

print(aStarSearch())


