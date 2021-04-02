#jawaban nomer 2


#basa basi dulu
print('berikut adalah program untuk mengonversi nilai Anda')

#nanya nanya aje
x= str (input('siapakah nama kamu?'))
y= float (input('berapakah nilai kamu?'))

#gaslgsgkehasil
info = 'halo,'+str( x )+'! nilai kamu setelah dikonversi adalah '
if y<60:
    print(info + ' E' )
elif 60<=y<=64:
    print(info+ 'C')
elif 65<=y<=69:
    print(info+ 'C+')
elif 70<=y<=74:
    print(info+ 'B')
elif 75<=y<=79:
    print(info+ 'B+')
elif 80<=y<=84:
    print(info+ 'A-')
elif 85<=y<=100:
    print (info+ 'A')
else:
    print('nilainya tidak valid!!!')

