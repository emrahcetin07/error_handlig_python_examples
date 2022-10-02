try:
   x=int(input('x:'))
   y=int(input('y:'))
   print(x/y)

except ZeroDivisionError:
    print('y icin 0 girilemez')

except ValueError:
    print('x ve y ici sayisal deger girmelisiniz')
