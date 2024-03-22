
import math
import heapq

coordinates = {}
adjList = {}

with open('input.txt','r') as f:
    vertex = int(f.readline())
    for i in range(vertex):
        lineStr = f.readline().split(' ')
        node ,x ,y = lineStr[0] ,int(lineStr[1]) ,int(lineStr[2])
        coordinates[node] = (x,y)
        adjList[node] = []
    edge = int(f.readline())
    for i in range(edge):
        lineStr = f.readline().split()
        fromNode, toNode, weight = lineStr[0],lineStr[1],int(lineStr[2])
        adjList[fromNode].append((toNode,weight))
    startNode = f.readline().rsplit()
    goaLNode = f.readline().rsplit()

def heuristic(x1,y1):
    return math.sqrt((x1-coordinates[goaLNode[0]][0])**2+(y1-coordinates[goaLNode[0]][1])**2)

class State:
    def __init__(self,node,g,parent):
        self.node = node
        self.g = g
        self.f = g + heuristic(coordinates[node][0],coordinates[node][1])
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f



q = []

startState = State(startNode[0],0,None)
heapq.heappush(q,startState)

while q:
    currState = heapq.heappop(q)
    if currState.node == goaLNode[0]:
       ans = []
       while currState is not None:
           ans.append(currState.node)
           currState = currState.parent
       break

    for neighbour in adjList[currState.node]:
        gnew = currState.g + neighbour[1]
        newState = State(neighbour[0],gnew,currState.node)
        heapq.heappush(q,newState)

for x in ans:
    print(x)





