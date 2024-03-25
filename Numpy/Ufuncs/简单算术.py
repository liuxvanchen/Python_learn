import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([5,6,7,8,9])
#下面是加减乘除
newarr=np.add(x,y)
print(newarr)

newarr2=np.subtract(y,x)

newarr3=np.multiply(x,y)

newarr4=np.divide(y,x)

miarr=np.power(x,y)

modarr=np.mod(x,y)
modarr2=np.remainder(x,y)

#返回商和模
arr=np.divmod(x,y)

#返回绝对值
z=np.array([-1,-5,89,2])
jueduiarr=np.absolute(z)

print(newarr,'\n',newarr2,'\n',newarr3,'\n',newarr4,'\n',miarr,'\n',modarr,'\n',modarr2,'\n',arr,'\n',jueduiarr)
