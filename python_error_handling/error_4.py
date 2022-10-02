def faktoriyel(x):
    x=int(x)

    if x < 0:
        raise ValueError('negatif deger')
    result = 1

    for i in range(1, x+1):
        result*=i

    return result


for x in [1,2,30,-6,'a11']:
    try:
        y=faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
     