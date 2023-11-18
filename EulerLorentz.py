import numpy as np
import matplotlib.pyplot as plt

def funx(xx,yy):
    kons = 10.0
    return kons*yy - kons*xx
def funy(xx,yy,zz):
    r = 28
    return r*xx - yy - xx*zz
def funz(xx,yy,zz):
    b = 8.0/3.0
    return xx*yy - b*zz

x0 = -1.0
y0 = 2.0
z0 = 7.0
t0 = 0.0
dt = 0.001
tmax = 500000 
datax = []
datay = []
dataz = []
for i in range(tmax):
    t = t0 + dt
    x = x0 + funx(x0,y0)*dt
    y = y0 + funy(x0,y0,z0)*dt
    z = z0 + funz(x0,y0,z0)*dt
    t0 = t
    x0 = x
    y0 = y
    z0 = z
    datax.append(x0)
    datay.append(y0)
    dataz.append(z0)
    #print(t0, z0)
data = np.zeros([tmax,3])
data[:,0] = datax
data[:,1] = datay
data[:,2] = dataz
print(data)
plt.plot(dataz)
# plt.plot(datax,dataz)
plt.show()
