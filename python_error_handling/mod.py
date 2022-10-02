print('modul eklendi')


number=10
numbers=[1,2,3,4,5]
person={
    "name":"Ali",
    "age":"25",
    "city":"istanbul"
}

def func(x,y):
    bol=float(x)/float(y)
    if bol<2:
        bol=1
        print(f'bol:{bol}')
        
    else:
        return bol

    

class Person:
    def speak(self):
        print('I am speaking Turkish')