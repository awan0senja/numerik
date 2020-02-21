#penggunaan subplots
#sedikit berbeda dengan subplot
import matplotlib.pyplot as p
import numpy as n

x=n.arange(-5,6)
y1=x
y2=x**2
y3=x**3
y4=x**4

fig, ax=p.subplots(nrows=2,ncols=2,figsize=(10,10))
ax[0,0].plot(x,y1,"bo")
ax[0,1].plot(x,y2,"g^")
ax[1,0].plot(x,y3,"r-")
ax[1,1].plot(x,y4,".-")

#judul
ax[0,0].set_title("Kurva Linier")
ax[0,1].set_title("Kurva Kuadratik")
ax[1,0].set_title("Kurva polinom tiga")
ax[1,1].set_title("Kurva Polinom Empat")

p.suptitle("Latihan Kurva keempat")
p.show()
