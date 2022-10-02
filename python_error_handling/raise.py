import string

def checkPassword(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]",psw):
        raise Exception("parola kücük harf icermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola BUYUK harf icermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam icermelidir")
    elif not re.search("[+-?]",psw):
        raise Exception("parola özel karakter icermelidir")
    elif re.search("\s",psw):
        raise Exception("parola bosluk icermez")

print('parola giriniz')

while password==True:
    password=input()
    

    try:
      checkPassword(password)
    except Exception as ex:
     print(ex)
