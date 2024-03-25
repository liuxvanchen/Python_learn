import numpy as np

x=[1,2,3,4]
y=[1,2,3,4]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

z2=np.add(x,y)
print(z2)