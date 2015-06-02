import sys

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
                if state[x] == 1 and state[self.sizeX + y]:
                    sys.stdout.write('*')
                else:
                    sys.stdout.write('.')
            print ""
        print "  " + str(self.getAction(state))

    def iterate(self, inState):
        currentX = 0
        currentY = 0
        for x in range(self.sizeX):
            if inState[x] == 1:
                currentX = x
                break
        for y in range(self.sizeY):
            if inState[self.sizeX + y] == 1:
                currentY = y
                break
        print currentX, currentY
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
        for a in range(self.actions):
            if state[self.sizeX + self.sizeY + a] == 1:
                return a + 1
        return 0

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


if __name__ == '__main__':
    w = World()
    s = w.getStartState()
    w.printState(s)
    s1 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
    w.printState(s1)
    s2 = w.iterate(s1)
    w.printState(s2)
    s3 = w.iterate(s1)
    w.printState(s3)
