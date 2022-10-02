
while True:
    sayi=input('sayı:')
    if sayi=='q':
        break
    try:
        result=float(sayi)
        print('girdiginiz sayi:',result)
    except ValueError:
          print('gecersiz sayi')
    continue