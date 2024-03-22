import copy
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

with open('input.txt','r') as f:
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

def getLowestCostSuccessor(state):
    for i in range(3):
        for j in range(3):
            if(state[i][j]==0):
                moveState = state
                mini = 10**10


                if(i!=0):
                    upState = swap(state,i,j,i-1,j)
                    upStateHeu = min(heu1(upState),heu2(upState))
                    if(upStateHeu < mini):
                        mini = upStateHeu
                        moveState = copy.deepcopy(upState)
                        print('UP')


                if(i!=2):
                    downState = swap(state,i,j,i+1,j)
                    downStateHeu = min(heu1(downState),heu2(downState))
                    if (downStateHeu < mini):
                        mini = downStateHeu
                        moveState = copy.deepcopy(downState)
                        print('DOWN')


                if(j!=0):
                    leftState = swap(state,i,j,i,j-1)
                    leftStateHeu = min(heu1(leftState),heu2(leftState))
                    if (leftStateHeu < mini):
                        mini = leftStateHeu
                        moveState = copy.deepcopy(leftState)
                        print('LEFT')

                if(j!=2):
                    rightState = swap(state,i,j,i,j+1)
                    rightStateHeu = min(heu1(rightState),heu2(rightState))
                    if (rightStateHeu < mini):
                        mini = rightStateHeu
                        moveState = copy.deepcopy(rightState)
                        print('RIGHT')
                return moveState,mini
    return 0

def hillChilbing(startState):
    curr = startState
    itr = 0
    while True:
        itr += 1
        if itr >= 1000 : break
        neighbour, heuristic = getLowestCostSuccessor(curr)
        print(neighbour,heuristic)

        if min(heu1(neighbour),heu2(neighbour)) > min(heu1(curr),heu2(curr)):
            return curr
        curr = neighbour

    print(curr)

print(hillChilbing(startState))

