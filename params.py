import numpy as np
############
#world params
a=30
b=30
world=np.zeros((a,b))
world[:,0]=1
world[0,:]=1
world[:,a-1]=1
world[b-1,:]=1
world[10,0:10]=1
world[5:10,10]=1
world[25:30,25]=1
world[15:18,15:18]=1
world[3:7,21:24]=1

targ=np.array([28.,28.])
thresh=3
nfeatsx=100
nfeatsy=100
v=6.
dt=0.2
################
#Q learning params
Nruns=5
alpha=0.1
gamma=0.9
lambd=0.9
epsilon=0.3
episodes=1000
A=9
highreward=100
penalty=-100
livingpenalty=-10
breakthresh=10000
evalruns=100
evalsteps=100