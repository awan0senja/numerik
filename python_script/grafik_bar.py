#Bentuk Plotting Bar Grafik
import matplotlib.pyplot as plt
import numpy as np

div=["Jombang","Kediri","Mojokerto","Surabaya","Gresik"]
nil1=[45,87,93,67,28]
nil2=[23,76,39,76,82]
var=[10,15,20,5,9]

index=np.arange(5)
lebar=0.30

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.bar(div,nil1,color="green")
plt.title("Jumlah Kelulusan Sekolah")
plt.xlabel("Kota")
plt.ylabel("Jumlah Kelulusan")

plt.subplot(2,2,2)
plt.barh(div,nil1,xerr=var,color="blue")
plt.title("Jumlah Kelulusan Sekolah")
plt.xlabel("Jumlah Kelulusan")
plt.ylabel("Kota")

plt.subplot(2,2,3)
plt.bar(index,nil1,lebar,color="green",label="SMP")
plt.bar(index+lebar,nil2,lebar,color="blue",label="SMA")
plt.title("Grafik Kelulusan")
plt.ylabel("Nilai")
plt.xlabel("Kota")
plt.xticks(index+lebar/2,div)

plt.subplot(2,2,4)
plt.bar(index,nil1,lebar,color="blue",label="SMP")
plt.bar(index,nil2,lebar,color="red",label="SMA",bottom=nil1)
plt.title("Grafik Kelulusan")
plt.ylabel("Nilai")
plt.xlabel("Kota")
plt.xticks(index,div)

plt.suptitle("Kondisi Perbandingan")
plt.legend(loc="best")
plt.show()
