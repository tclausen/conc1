import sys
import random

class World:
    sizeX = 3
    sizeY = 3
    actions = 4

    def printState(self, state):
        if len(state) != self.sizeX + self.sizeY + self.actions:
            raise Exception('Wrong state size ' + str(len(state)) + ' != ' + str(self.sizeX + self.sizeY + self.actions))
        print "State:"
        for y in range(self.sizeY):
            sys.stdout.write('  ')
            for x in range(self.sizeX):
                if state[x] == 1 and state[self.sizeX + y] == 1:
                    sys.stdout.write('*')
                else:
                    sys.stdout.write('.')
            print ""
        print "  action: " + str(self.getAction(state))

    def getXY(self, state):
        currentX = 0
        currentY = 0
        maxX = state[0]
        maxY = state[self.sizeX]
        for x in range(1,self.sizeX):
            if state[x] > maxX:
                currentX = x
                maxX = state[x] 
        for y in range(1,self.sizeY):
            if state[self.sizeX + y] > maxY:
                currentY = y
                maxY = state[self.sizeX + y] 
        return (currentX, currentY)

    def iterate(self, inState):
        (currentX, currentY) = self.getXY(inState)
        #print currentX, currentY
        action = self.getAction(inState)
        outState = self.getEmptyState()
        outState[currentX] = 1
        outState[currentY + self.sizeX] = 1
        if action != 0:
            outState[self.sizeX + self.sizeX + action - 1] = 1
        if action == 0:
            return outState
        if action == 1: # right
            if currentX < self.sizeX:
                outState[currentX] = 0
                outState[currentX + 1] = 1
        elif action == 2: # down
            if currentY < self.sizeY:
                outState[self.sizeX + currentY] = 0
                outState[self.sizeX + currentY + 1] = 1
        elif action == 3: # left
            if currentX > 0:
                outState[currentX] = 0
                outState[currentX - 1] = 1
        elif action == 4: # up
            if currentY > 0:
                outState[self.sizeX + currentY] = 0
                outState[self.sizeX + currentY - 1] = 1
        return outState

    def getAction(self, state):
        max = 0.5 # Make sure that at least one number is larger then 0.5 for a to be different from 0
        maxA = 0
        for a in range(self.actions):
            if state[self.sizeX + self.sizeY + a] > max:
                max = state[self.sizeX + self.sizeY + a]
                maxA = a
        return maxA + 1

    def getStartState(self):
        state = self.getEmptyState()
        state[0] = 1
        state[self.sizeX] = 1
        return state

    def getEmptyState(self):
        state = []
        for i in range(self.sizeX + self.sizeY):
            state.append(0)
        for i in range(self.actions):
            state.append(0)
        return state

    def setRandomAction(self, state):
        a = random.randint(0,4)
        #print "Random action: " + str(a)
        for i in range(self.actions):
            if i == a-1:
                state[self.sizeX + self.sizeY + i] = 1
            else:
                state[self.sizeX + self.sizeY + i] = 0


if __name__ == '__main__':
    w = World()
    s = w.getStartState()
    w.printState(s)
    s1 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
    w.printState(s1)
    print s1
    s2 = w.iterate(s1)
    print s2
    w.setRandomAction(s2)
    print s2
    w.setRandomAction(s2)
    print s2
    w.setRandomAction(s2)
    print s2
    w.setRandomAction(s2)
    print s2
    w.printState(s2)
    s3 = w.iterate(s1)
    w.printState(s3)
