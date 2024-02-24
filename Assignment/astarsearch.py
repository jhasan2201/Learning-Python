
coordinates = {}
adjList = {}

with open('input.txt', 'r') as f:
    vertex = int(f.readline())
    for i in range(vertex):
        lineStr = f.readline().split(' ')
        nid, x, y = lineStr[0], int(lineStr[1]), int(lineStr[2])
        coordinates[nid] = (x,y)
        adjList[nid] = []
    edges = int(f.readline())
    for i in range(edges):
        lineStr = f.readline().split()
        nid, nto, wei = lineStr[0], lineStr[1], int(lineStr[2])
        adjList[nid].append((nto,wei))
    startNid = f.readline().rsplit()
    goalNid = f.readline().rsplit()

import math
def heuristicFun(x1, y1):
    return math.sqrt((x1-coordinates[goalNid[0]][0])**2 + (y1-coordinates[goalNid[0]][1])**2)

class state:
    def __init__(self, nid, g, parent):
        self.nid=nid
        self.g = g
        self.f = g + heuristicFun(coordinates[nid][0], coordinates[nid][1])
        self.parent = parent

    # def __it__(self,other):
    #     return self.f < other.f

    def __lt__(self,other):
        return self.f < other.f

ans = []

startState = state(startNid[0], 0, None)


import heapq

q = []
heapq.heappush(q,startState)

while q:
    currStage = heapq.heappop(q)
    if (currStage.nid == goalNid[0]):
        while currStage is not None:
            ans.append(currStage.nid)
            currStage = currStage.parent
        break

    for neighbour in adjList[currStage.nid]:
        gnew = currStage.g + neighbour[1]
        newState = state(neighbour[0], gnew, currStage)
        heapq.heappush(q, newState)


ans.reverse()
for x in ans:
    print(x)