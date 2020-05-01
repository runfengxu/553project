import numpy as np

set = [1,1,1,0,1,1,0,0,0,1]

i=0
DCG=0
iDCG=0
one_count = 0
while(i<len(set)):
    if(set[i]==1):
        DCG = DCG + 1/np.log2(1+(i+1))
        one_count = one_count+1
    i=i+1
print(DCG)

i=0
while(i<one_count):
    iDCG = iDCG + 1/np.log2(1+(i+1))
    i=i+1
print(iDCG)

nDCG=DCG/iDCG
print(nDCG)

