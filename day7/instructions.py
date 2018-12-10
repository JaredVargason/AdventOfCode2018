#create edge matrix
edgeMatrix = [[False for i in range(26)] for j in range(26)]
with open('input.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        index1 = ord(words[1]) - ord('A')
        index2 = ord(words[7]) - ord('A')

        edgeMatrix[index1][index2] = True 

visited = []

#determine start nodes
frontier = set()
for toNode in range(len(edgeMatrix[0])): 
    startNode = True 
    for fromNode in range(len(edgeMatrix)):
        if edgeMatrix[fromNode][toNode]:
            startNode = False
    
    if startNode:
        frontier.add(toNode)

def ready_to_visit(nodeIndex):
    for fromNode in range(len(edgeMatrix)):
        if edgeMatrix[fromNode][nodeIndex] and fromNode not in visited:
            return False
    return True

def p1():
    while len(frontier) > 0:
        minIndex = min(frontier)
        frontier.remove(minIndex)
        visited.append(minIndex)

        for toNode in range(len(edgeMatrix[0])):
            if edgeMatrix[minIndex][toNode] and toNode not in visited and ready_to_visit(toNode):
                
                frontier.add(toNode)
        
        
        instructions = list(map(lambda t: chr(t + ord('A')), visited))
        print(str.join('',instructions))

class Step:
    def __init__(self, stepNum, startTime):
        self.stepNum = stepNum
        self.startTime = startTime 
        self.endTime = startTime + 61 + stepNum

def p2():
    NUM_ELVES = 5
    elf_steps = [None] * NUM_ELVES

    done = False
    time = 0

    while not done:
        finished_steps = [] 
        
        for i, step in enumerate(elf_steps):
            if step == None: #assign new jobs
                if len(frontier) > 0:
                    minIndex = min(frontier)
                    frontier.remove(minIndex)
                    elf_steps[i] = Step(minIndex, time)

            elif time == step.endTime:
                finished_steps.append(step.stepNum)
                visited.append(step.stepNum)
                elf_steps[i] = None                
            
        
        for job in finished_steps:
            for toNode in range(len(edgeMatrix[0])):
                if edgeMatrix[job][toNode] and toNode not in visited and ready_to_visit(toNode):
                    frontier.add(toNode)

        time += 1

        done = True
        for step in elf_steps:
            if step != None or len(frontier) > 0: 
                done = False
    
    print(time)

p2()
                

        

        