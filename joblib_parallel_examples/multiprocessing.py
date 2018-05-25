import multiprocessing
import numpy as np
from joblib import Parallel,delayed

def ProcessZ(VectorofLists,i,numprocs,W,leftovers):
    initiali=int(i)
    i=i*int(len(VectorofLists)/numprocs)
    leftover=leftovers[initiali]
    X,Y=YourFunction(VectorofLists[int(i):int(i)+int(len(VectorofLists)/numprocs)+int(leftover)],W)
    return [X,Y]

def YourFunction(V,W):
	V=np.array(V)
	W=np.array(W)
	print('Hello', np.dot(V,W.T))
	VectortoStore=[]
	for i in W:
		VectortoStore.append(np.dot(i,V.T))
	return [np.dot(V,W.T),VectortoStore]
def main():
	a=[1,1,1]
	b=[1,1,1]
	c=[1,1,1]
	d=[1,1,1]
	VectorofLists=[a,b,c,d]
	W=VectorofLists
	num_cores = multiprocessing.cpu_count()
	leftover=len(VectorofLists)%num_cores
	inputs=np.linspace(0,num_cores-1,num=num_cores)
	leftovers=[]
	for i in inputs:
		if i==len(inputs)-1:
		    leftovers.append(leftover)
		else:
		    leftovers.append(0)

	ReturnXY=Parallel(n_jobs=num_cores)(delayed(ProcessZ)(VectorofLists,i,num_cores,W,leftovers) for i in inputs)
	Xjoined=[]
	Yjoined=[]

	for i in ReturnXY:

		for ii in i[0]:


		    Xjoined.append(ii)
	for i in ReturnXY:

	#
		for ii in i[1]:

	#
		    Yjoined.append(ii)

	print(Xjoined,Yjoined)
main()
