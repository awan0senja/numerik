#Latihan Grafik dengan Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,5)
y=x**3


plt.figure(figsize=(10,10)) #ukuran kotak dari grafik, bukan pada sumbunya
plt.plot([1,2,3,4], [1,4,9,16],"go-",x,y,"r^-")
plt.title("Grafik Linier")
plt.xlabel("Kuadrat")
plt.ylabel("Sumbu X")
plt.show()

#Sumber: https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596
