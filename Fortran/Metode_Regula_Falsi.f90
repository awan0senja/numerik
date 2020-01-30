program bagidua
implicit none

!Deklarasi ariabel
real::a,b,c,fungsi
integer::i

!Inisialisasi Variabel
a=0
b=1
i=0

!Cetak Header
print*,
print*,'                       MENCARI NILAI AKAR DENGAN METODE REGULA FALSI'
print*,'-------------------------------------------------------------------------------------------------'
print*,
print*,' i       a          c          b         f(a)       f(c)       f(b)     Selang Baru     Lebarnya  '
print*,
print*,'-------------------------------------------------------------------------------------------------'

do while(abs(a-b)>0.00001)
c=b-(fungsi(b)*(b-a))/(fungsi(b)-fungsi(a))

if (abs(fungsi(c))<0.000001) then
a=c
b=c
end if

if (fungsi(a)*fungsi(c)<0) then
print '(i3,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,7x,a,7x,f9.6)',i,a,c,b,fungsi(a),fungsi(c),fungsi(b),'[a,c]',abs(a-c)
b=c
else
print '(i3,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,2x,f9.6,7x,a,7x,f9.6)',i,a,c,b,fungsi(a),fungsi(c),fungsi(b),'[c,b]',abs(c-b)
a=c
end if
i=i+1
end do

end program


function fungsi(x)
implicit none

real:: fungsi, x

fungsi=exp(x)-5*x**2

end function fungsi
