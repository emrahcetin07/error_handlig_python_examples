liste=["1","2","5a","100b","abc","10555","??12"]

for x in liste:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

    