import random
import math
import numpy as np
import matplotlib.pyplot as plt

x=[]
ciin=[]
sq=[]
k1=1
k=[k1]
n=0
i=0
j=0
num=25000
pi=[]
def ci(x):
    return (math.sqrt(1-(x**2)))
def sq1():
    return (round(random.uniform(-1,1),4))
def sq2():
    return (round(random.uniform(-1,1),4))



while k[n]!=num:
    while len(x)!=k[n]:
        x.append([sq1(),sq2()])
    while i!=k[n]:
        z=(math.sqrt((x[i][j])**2+(x[i][j+1])**2))
        c=ci(x[i][j])
        if z<1:
            ciin.append(round(z,4))
            i+=1
        elif (z>1 and x[i][j]==0):
            i+=1
        else:
            sq.append(round(z,4))
            i+=1
    n+=1
    k1+=1
    k.append(k1)
    piv= 4*(len(ciin)/len(x))
    pi.append(piv)
if len(k)!=len(pi):
    del k[-1]
print(round(pi[-1],4))
E= math.sqrt(((round(math.pi,4)-pi[-1])/math.pi)**2)
print("Relative Error=",round (E*100,3),"%")
plt.plot(k,pi)
plt.grid()
plt.xlabel("number of random points")
plt.ylabel("value of pi")
plt.show()
#--------Relative Error Calculations-------
