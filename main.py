from world import *
from nn import *

def error(s1, s2):
    e = 0
    for i in range(len(s1)):
        e = e + abs(s1[i] - s2[i])
    return e

# create world
w = World()

# create initial state
s = w.getStartState()

# create nn
nn = NN(len(s), 15, len(s))

# explore and create history for training
h = []
for i in range(20):
    w.setRandomAction(s)
    s1 = w.iterate(s)
    h.append([s, s1])
    s = s1
print h

# create initial state
s = w.getStartState()

# get new state from nn
s1 = nn.update(s) # Predicted next state
s2 = w.iterate(s) # Next state 
print s1
print s2
print error(s2, s1)

nn.train(h, 10000)

# get new state from nn
s1 = nn.update(s) # Predicted next state
s2 = w.iterate(s) # Next state 
print s1
print s2
print error(s2, s1)

# create evaluator


# iterate state N times (print error) and save in evaluator

# train nn on states in evaluator - print error

