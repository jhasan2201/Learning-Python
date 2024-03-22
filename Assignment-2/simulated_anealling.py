import copy
import random
import math
points = {
    0: (0,0),
    1: (0,1),
    2: (0,2),
    3: (1,0),
    4: (1,1),
    5: (1,2),
    6: (2,0),
    7: (2,1),
    8: (2,2)
}

startState = []

goalState = [[0,1,2],[3,4,5],[6,7,8]]

with open('input2.txt','r') as f:
    for i in range(3):
        lineStr = f.readline().split(' ')
        arr = []
        arr.append(int(lineStr[0]))
        arr.append(int(lineStr[1]))
        arr.append(int(lineStr[2]))
        startState.append(arr)

def heu1(state):
    misplaceTiles = 0
    for i in range(3):
        for j in range(3):
            if(state[i][j]!=goalState[i][j]):
                misplaceTiles+=1
    return misplaceTiles

def heu2(state):
    manhattenDistance = 0
    for i in range(3):
        for j in range(3):
           dis = abs(i-points[state[i][j]][0]) + abs(j-points[state[i][j]][1])
           manhattenDistance +=dis
    return manhattenDistance

def swap(state,i,j,a,b):
    newState = copy.deepcopy(state)
    newState[i][j] = newState[a][b]
    newState[a][b] = 0
    return newState

def randomSelectionSuccessor(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j]==0):
                choiceList = []
                if(i!=0):
                    choiceList.append(swap(state,i,j,i-1,j))
                if(j!=0):
                    choiceList.append(swap(state,i,j,i,j-1))
                if(i!=2):
                    choiceList.append(swap(state,i,j,i+1,j))
                if(j!=2):
                    choiceList.append(swap(state,i,j,i,j+1))
                return random.choice(choiceList)
    return state

# print(randomSelectionSuccessor(startState))

def schedule(t):
    if t >= 1000:
        return 0
    else:
        return 1000 - t


def simulatedAnnealing(startState):
    curr = startState
    random.seed(100)
    for t in range(1,1001):
        print(curr)
        T = schedule(t)
        if T==0 :
          return curr

        next = randomSelectionSuccessor(curr)

        delE = min(heu1(curr),heu2(curr)) - min(heu1(next),heu2(next))
        if(delE > 0):
            curr = next
            if(curr==goalState):
                return curr
        if(random.random() > math.exp(delE/T)):
            curr = next
            if(curr==goalState):
                return curr

        # time.sleep(3)
    return curr

print(simulatedAnnealing(startState))