program selangkecil
implicit none

!Inisialisasi variabel
real::a,b,y
real::x,h

!menentukan parameter variabel
a=-0.5 ! batas kiri
b=1.4 !batas kanan
h=0.1 !selang kenaikan

!menentukan nilai awal x dengan bergerak ke kanan
x=a 

print*,'---Akar Selang Kecil--'
print*,'----------------------'
print*,'   x           y      '
print*,'----------------------'

! proses pengulangan mencari akar
do while(x<=b)

! fungsi yang dicari nilai akarnya
y=exp(x)-5*(x)**2

! mencetak hasil di layar
print'(2x,f5.2,4x,f10.7)', x,y

! menaikkan nilai x
x=x+h
end do
print*,'----------------------'

end program selangkecil
