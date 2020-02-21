#grafik dengan bentuk subplot

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,11)
y1=x**3 - x**2 + x
y2=x**2

plt.figure(figsize=(9,9))
plt.subplot(2,2,1) #subplot(nrows,ncols,index(posisi grafik, mulai dari angka 1, dari kiri ke kanan))
plt.plot(x,y1,"g^-")
plt.title("Kurva pertama")

plt.subplot(2,2,4)
plt.plot(x,y2,"b.-")
plt.title("Kurva kedua")

plt.suptitle("Belajar menggambar kurva")
plt.show()
