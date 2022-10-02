turkce_karakterler='şçğüöıİ'
parola=input('parola:')
for i in parola:
    if i in turkce_karakterler:
        raise TypeError('Parola türkce karakter icermemeli')
    else:
        pass
    print('gecerli paralo')