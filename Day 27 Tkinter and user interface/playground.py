def add(*args): #this *args allows oyu to take in any number of inputs
    #you can also find specific positions by args[0]
    total = 0
    for n in args:
        total += n
    return total

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(2, add= 3, multiply= 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')#This get helps the code not break when something is called and not set. REturns none for value
        self.model = kw.get('model')

my_car = Car(make= 'Nissan')
print(my_car.make)
print(my_car.model)